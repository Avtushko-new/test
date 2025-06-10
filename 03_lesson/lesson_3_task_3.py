from address import Address
from mailing import Mailing

to_address = Address('220102', 'Минск', 'Алтайская', '64', '171')
from_address = Address('404152', 'Закутский', 'Мичурина', '12', '1')
mail = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=500,
    track="RR123456789RU"
)
output = (
        f"Отправление {mail.track} из {mail.from_address.index}, {mail.from_address.city}, "
    f"{mail.from_address.street}, {mail.from_address.house} - {mail.from_address.flat} в "
    f"{mail.to_address.index}, {mail.to_address.city}, {mail.to_address.street}, "
    f"{mail.to_address.house} - {mail.to_address.flat}. Стоимость {mail.cost} рублей."
)

print(output)
