# Lab 6

def print_menu():
    print("Menu ")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encoder(password):
    password_nums = list(password)
    encoded_password_list = []
    encoded_password = ""
    for num in password_nums:
        encoded_password_list.append(int(num) + 3)
    for item in encoded_password_list:
        encoded_password += str(item)
    return encoded_password
#print(encoder(str(12345555)))

def decoder(password):
    # write decoder here
    pass
#print(decoder(45678888))


def main():
    password = ""
    encoded_password = ""

    while True:
        menu_option = int(input("Please enter an option: "))


        if menu_option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encoder(password)
            print("Your password has been encoded and stored!")
            print()


        elif menu_option == 2:
            # add decoder here
            pass

        elif menu_option == 3:
            break


if __name__ == '__main__':
    main()

