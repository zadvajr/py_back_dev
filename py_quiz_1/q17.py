#What is the output of this code?
n = 4
total = 0
for i in range(1, n):
    for j in range(i + 1):
        if (i + j) % 3 == 0:
            total += 1
print(total)

#end
