from django.core.exceptions import ValidationError
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from lists.models import Item, List


# Create your views here.
def home_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html')


def view_list(request: HttpRequest, list_id: int) -> HttpResponse:
    list_ = List.objects.get(id=list_id)
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'], list=list_)
        return redirect(f'/lists/{list_.id}/')
    return render(request, 'list.html', {'list': list_})


def new_list(request: HttpRequest) -> HttpResponse:
    if request.POST:
        list_ = List.objects.create()
        item = Item.objects.create(text=request.POST['item_text'], list=list_)
        try:
            item.full_clean()
        except ValidationError:
            list_.delete()
            error = "You can't have an empty list item"
            return render(request, 'home.html', {"error": error})
        return redirect(f'/lists/{list_.id}/')
