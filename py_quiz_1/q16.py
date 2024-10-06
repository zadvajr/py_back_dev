#What is printed by the following code?
for i in range(5):
    if i == 2:
        continue
    for j in range(2):
        if i == j:
            break
        print(i, j)
#end
