from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Advertisement
from .forms import AdvertisementForm
from .forms import AdForm


def index(request):
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'index.html', context)


def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()

def create_ad(request):
    if request.method == 'POST':
        form = AdForm(request.POST)
    if form.is_valid():
            form.save()
            return redirect('your-success-page')
    else:
        form = AdForm()
    return render(request, 'create_ad.html', {'form': form})


    context = {'form': form}
    return render(request, 'advertisement-post.html', context)
