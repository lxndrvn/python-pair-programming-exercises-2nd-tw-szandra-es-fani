def fizzbuzz(number):
    x = number
    if x % 15 == 0:
        x = "FizzBuzz"
    elif x % 3 == 0:
        x = "Fizz"
    elif x % 5 == 0:
        x = "Buzz"
    else:
        x
    return x

def main():
    for x in range(1,101):
        fizzbuzz(x)
    return x

if __name__ == '__main__':
    main()

