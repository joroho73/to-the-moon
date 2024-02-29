from django.shortcuts import render
import requests


def company(request):
    return render(request=request, template_name="company_signup.html")

def address_lookup(request):
    return render(request=request, template_name="address_lookup.html")
