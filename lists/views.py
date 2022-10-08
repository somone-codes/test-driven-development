from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from lists.models import Item


# Create your views here.
def home_page(request: HttpRequest) -> HttpResponse:

    if request.POST:
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()

    return render(request, 'home.html', {
        'items': items,
    })
