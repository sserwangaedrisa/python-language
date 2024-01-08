# This code will print the hashes the user will tell it to 
def main():
    n = get_input()
    for i in range(n):
        print('#')

def get_input():
    while True:
        try:
            n = int(input("How many # do you want to print: "))
            if n > 0:
                return n
        except ValueError:
            print('Not an integer')

main()