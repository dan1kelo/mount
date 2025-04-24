from django.shortcuts import render

def homePage(request):
    return render(request, 'voin/home.html')


def itemsPage(request):
    return render(request, 'voin/items.html')


def roadPage(request):
    return render(request, 'voin/road.html')


def mountPage(request):
    return render(request, 'voin/mount.html')

def africaPage(request):
    return render(request, 'voin/africa.html')

def australiaPage(request):
    return render(request, 'voin/australia.html')


def asiaPage(request):
    return render(request, 'voin/asia.html')


def americaPage(request):
    return render(request, 'voin/america.html')


