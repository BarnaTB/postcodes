from pyexpat import model
import factory

from listings.models import Listing


class ListingFactory(factory.django.DjangoModelFactory):
    """Factory class to create test listings
    """
    class Meta:
        model = Listing
    
    id = 52957618
    name = "Central Wigan welcoming 2 bed Townhouse sleeps 6"
    host_id = 375437396
    host_name = "Susie"
    neighbourhood_group = "Wigan"
    neighbourhood = "Wigan District"
    latitude = 53.547343
    longitude = -2.635878
    price = 48.00
    minimum_nights = 2
    calculated_host_listings_count = 2
    availability_365 = 346
    number_of_reviews_ltm = 0
