from enum import unique
import requests

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from listings.api.renderers import OutcodeRenderer, OutcodesRenderer
from listings.models import Listing
from listings.api.serializers import ListingSerializer
from listings.utils import average, calculate_distance

from postcodes.utils.settings_utils import get_env_variable
from postcodes.utils.validators import validate_response


class RetrieveListingsView(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ListingSerializer
    renderer_classes = (OutcodeRenderer,)
    queryset = Listing.objects.all()

    def get(self, request, *args, **kwargs):
        outcode = kwargs.get("outcode")
        look_up_url = get_env_variable("POSTCODE_LOOKUP_BACKEND", required=True)
        response = requests.get(f"{look_up_url}/outcodes/{outcode}")
        response = response.json()
        validate_response(response)
        listings = self.queryset.filter(neighbourhood_group__in=response["result"]["admin_district"])
        listings_prices = [listing.price for listing in listings]

        average_listings_price = average(listings_prices, 2)

        response = {
            "average_listings_price": f"${average_listings_price}",
            "listing_count": len(listings)
        }
        return Response(response)


class RetrieveNearestPostcodeView(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ListingSerializer
    renderer_classes = (OutcodesRenderer,)
    queryset = Listing.objects.all()

    def get(self, request, *args, **kwargs):
        outcode = kwargs.get("outcode")
        look_up_url = get_env_variable(
            "POSTCODE_LOOKUP_BACKEND", required=True)
        response = requests.get(f"{look_up_url}/outcodes/{outcode}/nearest")
        response = response.json()
        validate_response(response)

        nexus_outcode = response["result"][0]
        nexus_outcode_coordinates = (
            nexus_outcode["latitude"], nexus_outcode["longitude"])

        outcodes = []

        admin_districts = [outcode["admin_district"]
                              for outcode in response["result"]]
        unique_districts = set().union(*admin_districts)

        nexus_listings = self.queryset.filter(neighbourhood_group__in=unique_districts)

        nexus_listings_prices = [listing.price for listing in nexus_listings]
        nexus_listing_average_price = average(nexus_listings_prices, round_to=2)
        nexus_listing_count = len(nexus_listings)

        for outcode in response["result"]:
            outcode_listings = [
                listing for listing in nexus_listings if listing.neighbourhood_group in outcode["admin_district"]]

            outcode_listing_prices = [listing.price for listing in outcode_listings]
            outcode_average_daily_price = average(outcode_listing_prices, 2)

            outcode_listings_count = len(outcode_listings)

            outcode_coordinates = (outcode["latitude"], outcode["longitude"])
            distance_from_nexus = calculate_distance(
                outcode_coordinates, nexus_outcode_coordinates, round_to=2)

            outcode = {
                "listing_count": outcode_listings_count,
                "average_daily_price": f"${outcode_average_daily_price}",
                "distance": distance_from_nexus
            }
            outcodes.append(outcode)
        
        response = {
            "nexus": nexus_outcode,
            "listing_count": nexus_listing_count,
            "average_daily_price": f"${nexus_listing_average_price}",
            "outcodes": outcodes
        }

        return Response(response)
