name = input()
price = int(input())
weight = int(input())
money = int(input())
print(f'''Чек
{name} - {weight}кг - {price}руб/кг
Итого: {price * weight}руб
Внесено: {money}руб
Сдача: {money - price * weight}руб''')