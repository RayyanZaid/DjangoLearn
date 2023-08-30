from django.shortcuts import render, HttpResponse

# Create routes here:

# request - allow us to access query parameters


def index(request):
    return HttpResponse("Hello World!")
