from typing import Counter


def loop_while():
    stop_value = int(input('What value do you want to stop at?: '))
    counter = 0
    two_pow = 1
    while two_pow<=stop_value:
        print(f'2^{counter} = {two_pow}')
        counter+=1
        two_pow=2**counter

def loop_for():
    power = int(input('Which power you want to rise 2?: '))
    for i in range(power):
        product = 2**i
        print(f'2 ^ {power} = {product}')


def main():
    loop_while()



if __name__=='__main__':
    print('Powers of 2'.center(35)+'\n')
    main()
