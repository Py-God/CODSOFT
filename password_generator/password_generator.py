import random
import string

def generator(length):
    if length < 95:
        # get rich string containing all required letters to use in generating password
        password_field = string.ascii_letters + string.digits + string.punctuation

        # generate password by getting a random combination of any length of the field
        password = "".join(random.sample(password_field, length))

        return password
    else:
        return "Password length must be less than 95 characters"

def main():
    print("Password Generator")
    print("------------------")
    # get and validate password length
    while True:
        try:
            password_length = int(input("Password Length: "))
        except ValueError:
            print("Password length should be an integer.")
            print()
        else:
            print(generator(password_length))
            print()


main()