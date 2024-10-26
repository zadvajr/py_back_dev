#While loop
#python has two primary loops: while and for
#count 1 to 10 and 10 to 1 with while loop

from time import sleep

i = 1
print("Counting 1 to 10...")
while i <= 10:
    print(i)
    sleep(1)
    i += 1

sleep(5)
i = 10
print("\n\n\nCounting backward 10 to 1....")
while i >= 1:
    print(i)
    sleep(1)
    i -= 1