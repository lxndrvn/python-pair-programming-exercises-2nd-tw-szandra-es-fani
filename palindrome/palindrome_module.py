import re

def palindrome(string):
    word = string.lower()
    word = re.sub(' ', '', word) 
    if str(word) == str(word)[::-1]: 
        return True
    else:
        return False

def main():
    return

if __name__ == '__main__':
    main()
