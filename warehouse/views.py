import random
from decimal import Decimal

from django.http import HttpResponse
from django.shortcuts import render

from . import models


# Create your views here.
def products(request):
    product_list = models.Sports_equipment.objects.all()

    return render(request, "warehouse/products.html", {"product_list": product_list})


NAMES = [
    "М'яч",
    "Ракетка",
    "Гантелі",
    "Скакалка",
    "Килимок",
    "Рукавиці",
    "Велошолом",
    "Штанга",
]
CATEGORIES = ["Футбол", "Теніс", "Фітнес", "Біг", "Йога", "Велоспорт", "Бокс"]
MATERIALS = ["Шкіра", "Пластик", "Сталь", "Гума", "Неопрен", "Карбон", "Бавовна"]
BRANDS = ["Nike", "Adidas", "Puma", "Reebok", "Wilson", "Under Armour", "Asics"]


def replenish(request, count):
    items = [
        models.Sports_equipment(
            name=f"{random.choice(NAMES)} {random.randint(1, 999)}",
            category=random.choice(CATEGORIES),
            material=random.choice(MATERIALS),
            brand=random.choice(BRANDS),
            price=Decimal(random.randint(100, 999999)) / 100,
        )
        for _ in range(count)
    ]
    models.Sports_equipment.objects.bulk_create(items)

    return render(request, "warehouse/replenish.html", {"count": count})


from django.contrib import messages
from django.shortcuts import redirect, render

from . import models


def add_product(request):
    if request.method == "POST":
        models.Sports_equipment.objects.create(
            name=request.POST["name"],
            category=request.POST["category"],
            material=request.POST["material"],
            brand=request.POST["brand"],
            price=request.POST["price"],
        )
        messages.success(request, "Товар додано")
        return redirect("products")

    return render(request, "warehouse/add_product.html")
