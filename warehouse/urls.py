from django.urls import path

from . import views

urlpatterns = [
    path("products/", views.products, name="products"),
    path("replenish/<int:count>", views.replenish),
    path("add_product/", views.add_product),
]
