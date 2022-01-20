def simetricP(setR):
    for tuple in setR:
        print(tuple)

def main():
    setR = read_file('./relations/r1.txt')
    simetricP(setR)

def read_file(file_name):
    try:
        with open(file_name, 'r', encoding='UTF-8') as f:
            # setR = []
            setb=()
            for line in f:
                # setR.append(tuple(line.strip(')(\n')))
                # Nested tuples: adding tuples inside tuple 'setb'
                setb= setb + ( tuple(map( int ,  line.strip(')(\n').split(','))  ) ,)
            return setb
    except:
        print('There was an exception')


if __name__ == '__main__':
    main()
