import random
from decimal import Decimal

from django.http import HttpResponse
from django.shortcuts import render

from . import models


# Create your views here.
def products(request):
    product_list = models.Sports_equipment.objects.all()

    html = f"""<table>
        <thead>
            <tr>
                <th>Назва</th>
                <th>Категорія</th>
                <th>Матеріал</th>
                <th>Бренд</th>
                <th>Ціна</th>
            </tr>
        </thead>
        <tbody>
        """
    for p in product_list:
        html += f"""<tr>
                <td>{p.name}</td>
                <td>{p.category}</td>
                <td>{p.material}</td>
                <td>{p.brand}</td>
                <td>{p.price}</td>
            </tr>"""

    html += "</tbody></table>"

    return HttpResponse(html)


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
            # від 1.00 до 9999.99 (вкладається в max_digits=6, decimal_places=2)
            price=Decimal(random.randint(100, 999999)) / 100,
        )
        for _ in range(count)
    ]
    models.Sports_equipment.objects.bulk_create(items)

    return HttpResponse(f"Додано {count} нових записів")
