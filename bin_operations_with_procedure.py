

def multiplication():
    # base = int(input('In wich base are you working on?: '))
    # a = int(input('Type the first number please: '), base)
    # b = int(input('Type the second number please: '), base)
    a = input('Type the first number please : ')
    b = input('Type the second number please: ')
    # tuple_range = (range(len(b)),  b)
    
    a_for_printing = ' '.join(list(a))
    bar = '\u2500'*len(a)+ '\u2500'*3
    #print a bar and factors
    print(f'{a:>30}\n{"x "+b:>30}\n{bar:>30}')

    # operations=''
    #print the procedure
    for i, digit in zip(range(0,len(b)),  b[::-1]):
        if digit=='1':
            print(f'{a_for_printing +" ":>{30-i*2}}')
        else:
            print(f'{len(a)*"0 ":>{30-i*2}}')
    product = bin(int(a,2)*int(b,2))[2:]
    # print(' '*29 + '\u2500'*len(product*2))
    bar = '\u2500'*4+'\u2500'*2*len(product)
    #print bar and producta
    print(f'{bar:>30}')
    product = ' '.join(list(product))
    print(f'{product+" ":>30}')




def divition():
    pass


def substraction():
    a = input('Type the minuend   : ')
    b = input('Type the subtrahend: ')
    bar = '\u2500'*len(a)+ '\u2500'*3
    difference = int(a,2)-int(b,2)
    if difference <0:
        base = 4
        difference = (1<<base) + difference
    print(f'{a:>30}\n{"- "+b:>30}\n{bar:>30}\n{difference:>30b}')
    
    print('\n' + b + ' ==> ')
    twos_complement(int(b,2),4)
    print(f'{"+ "+a:>37}\n{bar:>37}\n{difference:>37b}')



def twos_complement(a, bits):
    a = ((1<<bits)-1) ^ a
    print(f'ones = {a:>30b}\n')
    a +=1
    print(f'twos = {a:>30b}')
    return a




def main():
    options_menu='''
    [1] Multiplication
    [2] Divition
    [3] Substraction
    
    Choose an option: '''
    option = input(options_menu)
    # try:
    if option == '1':
        multiplication()
    elif option =='2':
        divition()
    elif option =='3':
        substraction()
    elif option == '4':
        twos_complement(-4,8)   
    else:
        print('Choose a correct option')
    # except:
        # print('There has been an exception')



if __name__== '__main__':
    main()