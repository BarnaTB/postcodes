import csv

from listings.managers import ListingManager

from listings.models import Listing


def upload_listings(reader: csv.DictReader):
    """Celery task to asynchronously upload a batch of listings
    Args:
        reader ([csv.DictReader]): Listings CSV dictionary reader object
    """
    listing_manager = ListingManager(batch_size=500)

    for row in list(reader):
        formatted_row = {key: value for key, value in row.items() if value and value.strip()}
        listing = Listing(**formatted_row)
        listing_manager.add(listing)
    listing_manager.done()
