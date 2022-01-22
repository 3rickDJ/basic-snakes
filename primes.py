def is_prime(number):
    for i in range(number-1,1,-1):
        if number%i==0:
            return False
    return True



def main():
    last_number = int(input('Until what number do you want to search?: '))
    for number in range(2, last_number+1):
        if is_prime(number):
            print(f' {number} is a prime number.')
        else:
            print(f' {number} is not a prime number.')


if __name__ == '__main__': 
    main()

    
    # last_number = int(input('Until what number do you want to search?: '))
    # for i in range(2,last_number):
    #     counter = 0
    #     for n in range(i-1,0,-1):
    #         if i%n ==0:
    #             counter+=1
    #    if counter>1:
    #        continue
    # print(f' {i} is a prime number.')


