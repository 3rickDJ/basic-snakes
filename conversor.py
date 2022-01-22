

menu = """
Welcome to the currency changer 🕋💰

1 - Colombian pesos
2 - Mexican pesos
3 - Argentine pesos

Choose an option: \
"""
option = input(menu)

def change_currency(dolar_value, currency):
    pesos = float(input('How many ' +currency + ' pesos do you have?: '))
    dolars = str(round(float(pesos/dolar_value), 2))
    print('You currently have $'+ dolars+' dollars')



if option =='1':
    change_currency(3875, 'colm')
elif option=='2':
    change_currency(24, 'mxn')
elif option=='3':
    change_currency(65, 'arg')
else:
    print('Please choose a correct option...')