from django.shortcuts import render, redirect, get_object_or_404

from store.models import Product
from store.forms import ProductForm


def product_list(request):
    products = Product.objects.all()
    return render(request, "store/product_list.html", {"products": products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "store/product_detail.html", {"product": product})


def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("store:product_list")
    else:
        form = ProductForm()
    return render(request, "store/product_create.html", {"form": form})


def product_edit(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("store:product_list")
    else:
        form = ProductForm(instance=product)
    return render(request, "store/product_edit.html", {"form": form})


def product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect("store:product_list")
