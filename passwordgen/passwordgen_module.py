import random

def passwordgen():
    
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    pw_length = random.randint(8, 20)
    mypw = ""
    for i in range(pw_length):
        next_index = random.randrange(len(alphabet))
        mypw = mypw + alphabet[next_index]
    return mypw
    print(mypw)


def main():
    return


if __name__ == '__main__':
    main()
