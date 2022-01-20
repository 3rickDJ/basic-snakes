def main():
    my_list = [2, "Four", False, -1.2]
    my_dict = {'firstname': 'Erick', 'lastname': 'De Jesus'}
    super_list = [
        {'firstname': 'Erick', 'lastname': 'De Jesus'},
        {'firstname': 'George', 'lastname': 'Cordero'},
        {'firstname': 'Veronica', 'lastname': 'Rodriguez'},
        {'firstname': 'Bob', 'lastname': 'Squarepants'},
        {'firstname': 'Blue', 'lastname': 'Perez'},
        {'firstname': 'Adriana', 'lastname': 'Molina'}
    ]
    super_dict = {
        "natural_num": [1,2,3,4,5,6,7,8,9,10],
        "interger_num": [-2,-1,0,-0,1,2],
        "floating_num": [1.7,1.8,1.9,2.0,2.1]
    }

    for key, value in super_dict.items():
        print(f'{key} {value}')
    print('-'*80)
    for element in super_list:
        print(f"{element['firstname']} {element['lastname']}")


if __name__ == '__main__':
    main()