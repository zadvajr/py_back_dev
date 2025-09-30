# Create a simple username and password authentication.
# If the username and password specified are correct, then print
# a success message, else print "You're are wrong!" five times.

user_name = "zadvajr"
password = "1059.dAz"

trials = 5
count = 0
while count < trials:
    username = input("Enter your username: ")
    passw = input("Enter your password: ")
    if username == user_name and passw == password:
        print("You logged in successfully!")
        break
    else:
        print("Wrong password!")
        count += 1