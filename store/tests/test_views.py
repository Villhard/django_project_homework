import pytest
from django.urls import reverse

from store.models import Product

pytestmark = pytest.mark.django_db


def test_product_list(client):
    url = reverse("store:product_list")

    resp = client.get(url)

    assert resp.status_code == 200


def test_product_create(client):
    url = reverse("store:product_create")

    resp = client.get(url)

    assert resp.status_code == 200


def test_product_edit(
    client,
    product,
):
    url = reverse("store:product_edit", args=[product.id])

    resp = client.get(url)

    assert resp.status_code == 200


def test_product_delete(
    client,
    product,
):
    url = reverse("store:product_delete", args=[product.id])

    resp = client.get(url)

    assert resp.status_code == 200


def test_product_detail(
    client,
    product,
):
    url = reverse("store:product_detail", args=[product.id])

    resp = client.get(url)

    assert resp.status_code == 200


def test_product_edit_not_found(client):
    url = reverse("store:product_edit", args=[999999])

    resp = client.get(url)

    assert resp.status_code == 404


def test_product_delete_not_found(client):
    url = reverse("store:product_delete", args=[999999])

    resp = client.get(url)

    assert resp.status_code == 404


def test_product_detail_not_found(client):
    url = reverse("store:product_detail", args=[999999])

    resp = client.get(url)

    assert resp.status_code == 404


def test_product_create_post(
    client,
    category,
):
    url = reverse("store:product_create")
    data = {
        "name": "Test Product",
        "description": "Test Description",
        "price": 100,
        "category": category.id,
    }

    resp = client.post(url, data=data)

    assert resp.status_code == 302
    assert resp.url == reverse("store:product_list")
    assert Product.objects.count() == 1


def test_product_create_post_invalid(client):
    url = reverse("store:product_create")
    data = {
        "name": "Te",
        "description": "Test Description",
        "price": 100,
        "category": 1,
    }

    resp = client.post(url, data=data)

    assert resp.status_code == 200
    assert Product.objects.count() == 0


def test_product_edit_post(
    client,
    product,
    category,
):
    url = reverse("store:product_edit", args=[product.id])
    data = {
        "name": "Updated Product",
        "description": "Updated Description",
        "price": 150,
        "category": category.id,
    }

    resp = client.post(url, data=data)

    assert resp.status_code == 302
    assert resp.url == reverse("store:product_list")
    assert Product.objects.count() == 1
    assert Product.objects.get(id=product.id).name == "Updated Product"
    assert Product.objects.get(id=product.id).description == "Updated Description"
    assert Product.objects.get(id=product.id).price == 150


def test_product_delete_post(
    client,
    product,
):
    url = reverse("store:product_delete", args=[product.id])
    resp = client.post(url)

    assert resp.status_code == 302
    assert resp.url == reverse("store:product_list")
    assert Product.objects.count() == 0
