from functools import reduce

def main():
    natural_to_square=[1,2,3,4,5,9,1]
    
    # natural_to_square=[i**2 for i in natural_to_square]
    # print(natural_to_square)

    odd = list(filter(lambda x: x%2!=0, natural_to_square))
    print(odd)

    square=list(map(lambda x: x**2 ,  natural_to_square))
    print(square)

    listOfTwo=[2,2,2,2,2]
    all_multiplied = reduce(lambda a,b: a*b, listOfTwo)
    print(all_multiplied)


if __name__ == '__main__':
    main()