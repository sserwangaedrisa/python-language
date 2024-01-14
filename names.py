import sys
names = ['Bill', 'Charlie', "Fred", 'George', "Percy", 'Ron']
name = input("What is the name you want: ")
for n in names:
    if name == n:
        print(f"found {n}")
        sys.exit(0)

print("Not found")
sys.exit(1)