from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

from .models import Listing

# Create your views here.


def index(request):

  listings = Listing.objects.all()
  paginator = Paginator(listings, 14)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
    'listings': paged_listings
  }
  return  render(request, 'listings/listings.html', context )

def listing(request):
  return  render(request, 'listings/listing.html')

def search(request):
  queryset_list = Listing.objects.order_by('VendorName')
#KEYWORDS
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(desciption__icontains=keywords)


  context= {
    'listings' :queryset_list
  }
  return  render(request, 'listings/search.html', context)