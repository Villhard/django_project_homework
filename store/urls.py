from django.urls import path

from store.views import (
    product_create,
    product_delete,
    product_detail,
    product_edit,
    product_list,
)

app_name = "store"

urlpatterns = [
    path("", product_list, name="product_list"),
    path("<int:product_id>/", product_detail, name="product_detail"),
    path("create/", product_create, name="product_create"),
    path("<int:product_id>/edit/", product_edit, name="product_edit"),
    path("<int:product_id>/delete/", product_delete, name="product_delete"),
]
