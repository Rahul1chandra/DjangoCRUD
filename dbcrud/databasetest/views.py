from __future__ import unicode_literals
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from databasetest.models import Place

def listing(request):
    place_list = Place.objects.all()
    paginator = Paginator(place_list, 2)
    page = request.GET.get('page')
    try:
        places = paginator.page(page)
    except PageNotAnInteger:
        places = paginator.page(1)
    except EmptyPage:
        places = paginator.page(paginator.num_pages)
    # import pdb
    # pdb.set_trace()
    return render(request, 'list.html', {'contacts': places})
