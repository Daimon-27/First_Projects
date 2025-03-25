receipt = {}
while True:
    products = input('Введіть через пробіл назву товару, його кількість та ціну: ').lower()
    if products == 'stop':
        break
    txt = products.split()
    receipt[txt[0]] = [int(txt[1]), int(txt[2])]

total_price_by_product = {}
the_most_expensive_product = ['', 0]

for k,v in receipt.items():
    total_price_by_product[k] = v[0] * v[1]
    if total_price_by_product[k] > the_most_expensive_product[1]:
        the_most_expensive_product = [k, total_price_by_product[k]]

total_price = 0

for i in total_price_by_product.values():
    total_price += i

print('Всі товари в чеку:')
for k,v in total_price_by_product.items():
    print(f'{k} - {v} грн')

print(f'\nНайдорожчий товар:\n{the_most_expensive_product[0]} - {the_most_expensive_product[1]} грн')
print(f'\nЗагальна сума - {total_price} грн')