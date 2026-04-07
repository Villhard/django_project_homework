import pytest

from store.models import Category, Product


@pytest.fixture
def category():
    return Category.objects.create(
        name="Test Category",
        description="Test Description",
    )


@pytest.fixture
def product(category):
    return Product.objects.create(
        name="Test Product",
        description="Test Description",
        price=100,
        category=category,
    )
