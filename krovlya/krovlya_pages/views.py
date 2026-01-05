from django.shortcuts import render

def main(request):
    return render(request, "main.html")

def contacts(request):
    return render(request, "contacts.html")
