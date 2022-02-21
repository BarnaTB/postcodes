import io
import csv
from django.shortcuts import redirect, render

from django.urls import path
from django.contrib import admin
from listings.forms import CsvUploadForm

from listings.models import Listing
from listings.tasks import upload_listings
from postcodes.utils.validators import validate_fields


@admin.register(Listing)
class ListingsAdmin(admin.ModelAdmin):
    
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):
        """Admin view that uploads a csv of listing data
        """
        form = CsvUploadForm(request.method, request.FILES)
        data = {"form": form}
        if request.method == 'POST':
            file = request.FILES['csv_file']
            decoded_file = file.read().decode()
            io_string = io.StringIO(decoded_file)
            required_fields = ("id", "name", "host_id", "host_name", "neighbourhood_group",
                               "neighbourhood", "latitude", "longitude", "room_type", "price",
                               "minimum_nights", "number_of_reviews", "last_review",
                               "reviews_per_month", "calculated_host_listings_count",
                               "availability_365", "number_of_reviews_ltm", "license")
            reader = csv.DictReader(io_string)
            is_valid = validate_fields(required_fields, tuple(reader.fieldnames))
            if not is_valid:
                return redirect("..")
            upload_listings(reader)
        return render(request, "admin/csv_upload.html", data)
