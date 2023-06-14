from polls.models import InventoryItem
from django.forms import ModelForm, TextInput

class InventoryItemsForm(ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['product', 'pallet', 'amount', 'update_time']
        widgets = {
            'product': TextInput
        }