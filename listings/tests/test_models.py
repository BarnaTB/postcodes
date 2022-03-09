from django.test import TestCase
from listings.models import Listing

from listings.tests.factories import ListingFactory


class ListingModelTestCase(TestCase):

    def test_create_listing(self):
        """Test that a Listing model instance successfully creates a listing 
        """
        listing = ListingFactory.create(
            id=50,
            name="Central Wigan welcoming 2 bed Townhouse sleeps 6",
            host_id=375437396,
            host_name="Susie",
            neighbourhood_group="Wigan",
            neighbourhood="Wigan District",
            latitude=53.547343,
            longitude=-2.635878,
            price=48.00,
            minimum_nights=2,
            calculated_host_listings_count=2,
            availability_365=346,
            number_of_reviews_ltm=0
        )

        self.assertIsInstance(listing, Listing)
        self.assertEqual(listing.id, 50)
        self.assertEqual(listing.price, 48.00)
        self.assertEqual(listing.neighbourhood_group, "Wigan")
