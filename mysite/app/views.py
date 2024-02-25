from django.shortcuts import render


def company(request):
    return render(request=request, template_name="company.html")
