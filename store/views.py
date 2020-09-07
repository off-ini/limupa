from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Artist, Contact, Album, Boocking
# Create your views here.

def index(request):
    albums = Album.objects.filter(avalible=True).order_by('-created_at')[:12]
    context = {'albums': albums}
    return render(request, 'store/index.html', context)

def listing(request):
    albums_list = Album.objects.filter(avalible=True)
    paginator = Paginator(albums_list, 3)
    page = request.GET.get('page')
    try:
        albums = paginator.get_page(page)
    except PageNotAnInteger:
        albums = paginator.get_page(1)
    except EmptyPage:
        albums = paginator.get_page(paginator.num_pages)
    context = {'albums': albums}
    return render(request, 'store/listing.html', context)

def detail(request, album_id):
    _id_ = int(album_id)
    try:
        album = Album.objects.get(id=_id_)
    except:
        return render(request, '404.html')
    context = {'album': album}
    return render(request, 'store/detail.html', context)

def search(request):
    query = request.GET.get('query')
    if not query:
       return listing(request)
    else:
        albums = Album.objects.filter(title__icontains=query)
        if not albums.exists():
            albums = Album.objects.filter(artists__name__icontains=query)
        if not albums.exists():
            return render(request, '404.html')
    context = {'albums': albums}
    return render(request, 'store/search_result.html', context)

