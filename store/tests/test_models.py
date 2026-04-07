import pytest

pytestmark = pytest.mark.django_db


def test_product_str(product):
    assert str(product) == product.name


def test_product_repr(product):
    assert repr(product) == (
        f"Product(name={product.name}, description={product.description}, "
        f"price={product.price}, category={product.category})"
    )


def test_category_str(category):
    assert str(category) == category.name


def test_category_repr(category):
    assert repr(category) == (
        f"Category(name={category.name}, description={category.description})"
    )
