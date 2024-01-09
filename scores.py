scores = []
for i in range(4):
    if True:
        try:
             x = int(input("What it the score: "))
        except ValueError:
            print("Not an integer")
    scores += [x]
    # we can also apend an element using the code bellow
    # scores.append(x)

average = sum(scores) / len(scores)
print(f"Average = {average}")




