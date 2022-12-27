from django.shortcuts import render

# Create your views here.
def HOMEPAGE(REQUEST):
    return render(REQUEST,"homepage.html")