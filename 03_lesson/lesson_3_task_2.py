from smartphone import Smartphone

catalog = [
    Smartphone('Apple', 'iPhone 12', '+79053215647'),
    Smartphone("Samsung", "Galaxy S24", "+79098765432"),
    Smartphone("Xiaomi", "Redmi Note 13", "+79567890123"),
    Smartphone("Google", "Pixel 8", "+79234567890"),
    Smartphone("OnePlus", "11 Pro", "+79345678901")
]


for smartphone in catalog:
    print(f'{smartphone.brand} - {smartphone.model}. {smartphone.tel_number}')
