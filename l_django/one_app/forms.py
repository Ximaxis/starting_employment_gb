from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    """
    Класс определяет форму создания товара
    """

    def __int__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Item
        fields = ('title', 'price',  'vendor',)

