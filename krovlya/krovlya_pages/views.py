from django.shortcuts import render

def main(request):
    return render(request, "main.html")

def contacts(request):
    return render(request, "contacts.html")

def business(request):
    return render(request, "for_business.html")

def service(request):
    return render(request, "services.html")

def delivery(request):
    return render(request, "delivery.html")

def about(request):
    return render(request, "about.html")


