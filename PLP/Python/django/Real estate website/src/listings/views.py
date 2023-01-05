from django.shortcuts import render, redirect

# Create your views here.

# CRUD - Create, retrieve, update and delete, list
from .models import listing
from .forms import ListingForm


def listing_list(request):
    listings = listing.objects.all()
    context = {
        "listings": listings,
    }
    print(listings)
    return render(request, "listings.html", context)


def listing_retrieve(request, pk):
    Listing = listing.objects.filter(id=pk).values()[0]
    print(Listing)
    context = {
        "estate": Listing,
    }
    print(listing)
    print(listing.title, listing.price, listing.address)
    print(context)

    return render(request, "listing.html", context)


def listing_create(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form,
    }
    return render(request, "listing_create.html", context)


def listing_update(request, pk):
    Listing = listing.objects.get(id=pk)
    form = ListingForm(instance=Listing)
    if request.method == "POST":
        form = ListingForm(request.POST, files=request.FILES, instance=Listing)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        "form": form,
    }
    return render(request, "listing_update.html", context)


def listing_delete(request, pk):
    Listing = listing.objects.get(id=pk)
    Listing.delete()
    return redirect("/")
