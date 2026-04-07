import pytest

from store.forms import ProductForm

pytestmark = pytest.mark.django_db


def test_product_form_valid(category):
    form = ProductForm(
        data={
            "name": "Test Product",
            "description": "Test Description",
            "price": 100,
            "category": category.id,
        }
    )
    assert form.is_valid()


def test_product_form_invalid(category):
    form = ProductForm(data={
        "name": "Te",
        "description": "Test Description",
        "price": 100,
        "category": category.id,
    })
    assert not form.is_valid()
