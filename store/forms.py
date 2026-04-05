from django import forms

from store.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "category"]
        labels = {
            "name": "Название",
            "description": "Описание",
            "price": "Цена",
            "category": "Категория",
        }

    def clean_name(self):
        name = self.cleaned_data["name"]
        if len(name) < 3:
            raise forms.ValidationError("Название должно быть не менее 3 символов")
        return name

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price <= 0:
            raise forms.ValidationError("Цена должна быть положительной")
        return price
