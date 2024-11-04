#What will this code output?
x = 1
for i in range(1, 4):
    for j in range(2, i + 3):
        if (i + j) % 2 == 0:
            x += i * j
print(x)

#end
