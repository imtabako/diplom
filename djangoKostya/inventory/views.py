from django.shortcuts import render
from polls.models import InventoryItem
from .forms import InventoryItemsForm


# Create your views here.
def edit(request):
    form = InventoryItemsForm()

    data = {
        'form': form,
    }
    return render(request, 'inventory/edit.html')


def ilist(request):
    return render(request, 'inventory/list.html')
