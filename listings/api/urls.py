from django.urls import path

from listings.api.views import RetrieveListings


urlpatterns = [
    path("outcode/<str:outcode>/", RetrieveListings.as_view(), name="retrieve_listings"),
]

