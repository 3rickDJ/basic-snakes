import random


def main():
    main_text = '''
            Guess the number

    Pick a number from 1 to 100 ! 
    '''
    print(main_text)
    # answer = random.choice(range(1,100))
    answer = random.randint(1,100)
    game(answer)

def game(answer):
    while True:
        user_answer = int(input('Pick a number: '))
        if user_answer == answer:
            print(f'You have won!!!\nThe number is {user_answer}')
            break
        
        if user_answer>answer:
            print(f'Is less than {user_answer}')
        else:
            print(f'Is greater than {user_answer}')


if __name__ == '__main__':
    main()