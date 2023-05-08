sum_tickets = 0
tickets = int(input("Введитете количество билетов: "))
for age in range (tickets):
    age = int(input("Введите возвраст посетителя: "))
        if age < 18:
        sum_tickets += 1
    elif 18 <= age <= 25:
        sum_tickets += 990
    elif age > 25:
        sum_tickets += 1390
    if sum_tickets > 3:
print("Сумма к оплате с учетом скидки: ", sum(tickets) - ((sum(tickets) / 100) * 10))
print("Сумма к оплате: ", sum(tickets), "рублей")
print("Стоимость ваших билетов: ", tickets)
