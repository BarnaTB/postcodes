from django.test.testcases import TestCase
from django.urls import reverse
from django.test import SimpleTestCase

from listings.tests.factories import ListingFactory


class RetrieveListingsTestCase(TestCase):

    def setUp(self):
        self.listing = ListingFactory()

    def test_retrieve_listings_successfully(self):
        """Test a user can retrieve listings data lying in an outcode
        """
        self.url = reverse("listings:retrieve_listings",
        kwargs={"outcode": "M11"}
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["listing_count"], 1)
    
    def test_retrieve_listings_no_data(self):
        """Test a user gets an appropriate error message when there's no data
        """
        self.url = reverse("listings:retrieve_listings",
                           kwargs={"outcode": "M11678"}
                           )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data["detail"], "Outcode not found")


class RetrieveNearestPostcodeViewTestCase(TestCase):
    def setUp(self):
        self.listing = ListingFactory()
        self.neighbouring_listing = ListingFactory(id=50, neighbourhood_group="Oldham")

    def test_retrieve_listings_successfully(self):
        """Test that a user can retrieve nearest listings to nexus outcode 
        nexus outcode
        """
        self.url = reverse("listings:retrieve_nearest_outcodes",
                           kwargs={"outcode": "M11"}
                           )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data["outcodes"])
        self.assertEqual(response.data["average_daily_price"], "$48.00")
        self.assertEqual(response.data["listing_count"], 2)

    def test_retrieve_listings_no_data(self):
        """Test that a user gets an appropriate error message when there's no data
        """
        self.url = reverse("listings:retrieve_nearest_outcodes",
                           kwargs={"outcode": "M11678"}
                           )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data["detail"], "Outcode not found")
