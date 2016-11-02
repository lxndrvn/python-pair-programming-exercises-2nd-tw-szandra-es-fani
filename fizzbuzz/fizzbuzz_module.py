def fizzbuzz(number):
    x = number
    if x % 15 == 0:
        x = "FizzBuzz"
    elif x % 3 == 0:
        x = "Fizz"
    elif x % 5 == 0:
        x = "Buzz"
    else:
        print(x)
    return x

def main():
    return True

if __name__ == '__main__':
    main()

