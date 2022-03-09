import requests

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from listings.api.renderers import ListingRenderer
from listings.models import Listing
from listings.api.serializers import ListingSerializer
from listings.utils import average

from postcodes.utils.exceptions import CustomAPIException
from postcodes.utils.settings_utils import get_env_variable
from postcodes.utils.validators import validate_response


class RetrieveListings(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ListingSerializer
    renderer_classes = (ListingRenderer,)
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



