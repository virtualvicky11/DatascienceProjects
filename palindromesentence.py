def is_palindrom_sentence(string):
    word =""
    for char in string:
        if char.isalnum():
            word+= char
    return word[::-1].casefold() == word.casefold()

sentence = input("Entrer the sentence to check palindrome :")

if is_palindrom_sentence(sentence):
    print('The provided sentence is palindrome')
else:
    print('The provided sentence is not palindrome')
