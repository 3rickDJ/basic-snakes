def palindrome(word):
    word = word.replace(' ', '').lower()
    inverted_word = word[::-1]
    if not word.isdigit() and inverted_word==word:
        return True
    else:
        return False


def run():
    word = input('Write a word: ')
    if palindrome(word):
        print('Is a palindrome')
    else:
        print('Is\'n a palindrome')


if __name__=='__main__':
    run()