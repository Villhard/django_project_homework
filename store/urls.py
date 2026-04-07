from django.urls import path

from store.views import (
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductListView,
    ProductUpdateView,
)

app_name = "store"

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("<int:product_id>/", ProductDetailView.as_view(), name="product_detail"),
    path("create/", ProductCreateView.as_view(), name="product_create"),
    path("<int:product_id>/edit/", ProductUpdateView.as_view(), name="product_edit"),
    path("<int:product_id>/delete/", ProductDeleteView.as_view(), name="product_delete"),
]
