# printing meow for the n times ' n is the number of times the user will input'
def main():
    n = int(input('How many times i should meow: '))
    for i in range(n):
        meow()


def meow():
    print('meow')

main()