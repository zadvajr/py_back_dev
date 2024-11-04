#What is the output of the following code?
for i in range(1, 4):
    for j in range(1, i + 1):
        if j % 2 == 0:
            print(i, j)
