# Create a simple username and password authentication.
# If the username and password specified are correct, then print
# a success message, else print "You're are wrong!" five times.

user_name = "zadvajr"
password = "1059.dAz"

<<<<<<< HEAD
trials = 5
=======
trials = 3
>>>>>>> f4a25dca34b2019639c08ef1f61b8e96cce26879
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