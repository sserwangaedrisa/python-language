x = int(input('Enter the number of hashes: '))
for i in range(x):
    for j in range(x):
        print('#',end='')
    print()

print("The second attempt is here")

for k in range(x):
    print('#'*x)