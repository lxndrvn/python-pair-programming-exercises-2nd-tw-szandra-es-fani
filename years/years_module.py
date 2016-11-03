import datetime
from datetime import date

def years(age):
    x = date.today().year
    y = 100 - age
    z = x + y
    print(z)
    return z

def main():
    name = input("Give me your name: ")
    print("Your name is " + name)
    age = int(input("How old are you? "))
    years(age)

if __name__ == '__main__':
    main()