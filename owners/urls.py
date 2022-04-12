from django.urls import path

from owners.views import OwnerView, DogView, OwnerDogView

urlpatterns = [
    path('owners',OwnerView.as_view()),
    path('dogs',DogView.as_view()),
    path('ownerdog',OwnerDogView.as_view())
]
