from django.urls import path
from . import views

# Connect views to a url


# paths to connect url to view
urlpatterns = [

    # when user goes to empty string, it will run the home function
    path("index", views.index, name="index")
]
