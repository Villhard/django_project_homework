from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from store.forms import ProductForm
from store.models import Product


class ProductListView(ListView):
    model = Product
    template_name = "store/product_list.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = "store/product_detail.html"
    context_object_name = "product"
    pk_url_kwarg = "product_id"


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "store/product_create.html"
    success_url = reverse_lazy("store:product_list")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "store/product_edit.html"
    success_url = reverse_lazy("store:product_list")
    pk_url_kwarg = "product_id"


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "store/product_delete.html"
    success_url = reverse_lazy("store:product_list")
    pk_url_kwarg = "product_id"
