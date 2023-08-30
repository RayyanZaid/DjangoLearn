from django.shortcuts import render, HttpResponse

import pyrebase

config = {
    apiKey: "AIzaSyBkVTJojqltZpA7q1MV1-acVrBpbnHSUis",
    authDomain: "sportstracker-a34a2.firebaseapp.com",
    projectId: "sportstracker-a34a2",
    storageBucket: "sportstracker-a34a2.appspot.com",
    messagingSenderId: "1039856420726",
    appId: "1:1039856420726:web:88f991282ff9444a855c57"
}


# Create routes here:

# request - allow us to access query parameters


def index(request):
    return HttpResponse("Hello World!")
