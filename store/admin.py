from django.contrib import admin
from django.db.models import F

from store.models import Category, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "category"]
    list_filter = ["category"]
    search_fields = ["name", "description"]
    actions = ["increment_price", "decrement_price"]

    @admin.action(description="Увеличить цену на 10%%")
    def increment_price(self, request, queryset):
        queryset.update(price=F("price") * 1.1)

    @admin.action(description="Уменьшить цену на 10%%")
    def decrement_price(self, request, queryset):
        queryset.update(price=F("price") * 0.9)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    search_fields = ["name", "description"]
