from pprint import pprint


def simetricP(setR):
    for tuple in setR:
        a,b= tuple
        if ((a,a) not in setR) or ((b,b) not in setR):
            return False
    return True


def reflexive(setR):
    for tuple in setR:
        a,b= tuple
        if (b,a) not in setR:
            return False
    return True


def main():
    setR = read_file('./relations/r1.txt')
    if simetricP(setR):
        print('Es simétrica')
    else:
        print('No es simétrica')
    
    if reflexive(setR):
        print('Es reflexiva')
    else:
        print('No es reflexiva')

    

def read_file(file_name):
    try:
        with open(file_name, 'r', encoding='UTF-8') as f:
            # setR = []
            setb=()
            for line in f:
                # setR.append(tuple(line.strip(')(\n')))
                # Nested tuples: adding tuples inside tuple 'setb'
                #getting out '()\n'; spliting it; turn them into intergers; 
                setb= setb + ( tuple( map( int,  line.strip(')(\n').split(',')) ) ,)
            return setb
    except:
        print('There was an exception')


if __name__ == '__main__':
    main()
