from decimal import Decimal
warehouse_data = [
    {'warehouse': 7, 'material': 'Mato', 'remainder': 12, 'price': Decimal('1500.00')},
    {'warehouse': 8, 'material': 'Mato', 'remainder': 200, 'price': Decimal('1600.00')},
    {'warehouse': 9, 'material': 'Ip', 'remainder': 40, 'price': Decimal('500.00')},
    {'warehouse': 10, 'material': 'Ip', 'remainder': 300, 'price': Decimal('550.00')},
    {'warehouse': 11, 'material': 'Tugma', 'remainder': 500, 'price': Decimal('300.00')},
    {'warehouse': 12, 'material': 'Zamok', 'remainder': 1000, 'price': Decimal('2000.00')}
]

material_totals = {}

for entry in warehouse_data:
    material = entry['material']
    remainder = entry['remainder']
    if material in material_totals:
        material_totals[material] += remainder
    else:
        material_totals[material] = remainder

print(material_totals)