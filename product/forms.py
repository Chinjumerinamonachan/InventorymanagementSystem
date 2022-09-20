from django import forms
from product.models import Product

# create/update form product
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price","description", "unit", "category","image"]

class AddToCartForm(forms.Form):
    product = forms.IntegerField()
    quantity = forms.IntegerField()