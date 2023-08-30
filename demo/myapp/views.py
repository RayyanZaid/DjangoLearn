from django.shortcuts import render, HttpResponse

# Create routes here:

# request - allow us to access query parameters


def index(request):
    print("Opened Index")
    return HttpResponse("Hello World!")
