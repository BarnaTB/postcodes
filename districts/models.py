from email.policy import default
from random import choices
from unicodedata import name
from django.db import models


class Listing(models.Model):

    class RoomType(models.TextChoices):
        ENTIRE_PLACE = 'Entire place/apt'
        SHARED_ROOM = 'Shared room'
        PRIVATE_ROOM = 'Private room'

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    host_id = models.IntegerField(null=True, blank=True)
    host_name = models.CharField(max_length=255, blank=False, null=False)
    neighbourhood_group = models.CharField(max_length=255)
    neighbourhood = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    room_type = models.CharField(
        max_length=20, choices=RoomType.choices, null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    minimum_nights = models.IntegerField(null=False, blank=True)
    number_of_reviews = models.IntegerField(null=False, blank=True)
    last_review = models.DateField(blank=True)
    calculated_host_listings_count = models.IntegerField()
    availability_365 = models.IntegerField()
    number_of_reviews_ltm = models.IntegerField()
    license = models.CharField(max_length=255, null=False, blank=False)
    