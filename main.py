
import random

file=open("words.txt",'r')
lis=file.read().split()
word_length=None

def get_choice():
    i=1
    while i==1:
        n=int(input("Enter the number of wrong guesses[1-25]: "))
        if n>=1 and n<=25:
            return n
            i=2
        else:
            print("Enter the value between [1-10]")


def get_word_length():
    i = 1
    while i == 1:
        n = int(input("Enter the word length[4-10]: "))
        if n >= 4 and n <= 10:
            return n
            i = 2
        else:
            print("Enter the value between [4-10]!")


def get_word():
    word=random.choice(lis)
    if len(word)>=word_length:
        return word
    return get_word()


def game(choice):
    word = get_word()
    str='*'*len(word)
    stack=[]
    print('')
    while choice!=0:
        if word == str:
            print("Hurray you got it right!!\nWord :",word)
            return
        print("Word :",str)
        print("Attempts remaining : ",choice)
        print("Previous guesses :",end=' ')
        for i in stack:
            print(i,end=' ')
        print('')
        letter=input("Choose the next letter : ")
        letter=letter.strip()
        if letter not in stack:
            if letter not in word:
                print(letter,'is not in the word!')
                choice-=1
                stack.append(letter)
            else:
                print(letter,'is in the word!')
                index=word.find(letter)
                str=str[:index]+letter+str[index+1:]
                stack.append(letter)
            print('')
        else:
            print(letter,"is already tried before\n")
    print("Sorry! You have 0 attempts left.")
    print("The word is :",word,'\n\n')


if __name__=='__main__':
    while(1):
        n=int(input("1.Play\t2.Exit\nEnter the choice : "))
        if n==1:
            choice=get_choice()
            word_length=get_word_length()
            game(choice)
        else:
            print("Thanks for playing!")
            exit(0)
