import sys
names = ['Bill', 'Charlie', "Fred", 'George', "Percy", 'Ron']
name = input("What is the name you want: ")
# for n in names:
#     if name == n:
#         print(f"found {n}")
#         sys.exit(0)

# print("Not found")
# sys.exit(1)
# The above code is the older way of doing it in c
# The newer version is here

if name in names:
    print('Found')
    sys.exit(1)

print('not foud')
sys.exit(0)