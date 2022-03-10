from django.urls import path

from listings.api.views import RetrieveListingsView, RetrieveNearestPostcodeView


urlpatterns = [
    path("outcode/<str:outcode>/", RetrieveListingsView.as_view(),
         name="retrieve_listings"),
    path("nexus/<str:outcode>/", RetrieveNearestPostcodeView.as_view(),
         name="retrieve_nearest_outcodes"),
]

