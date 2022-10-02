def main():
    num1 = input("Enter num1: ")
    num2 = input("Enter num2: ")

    if num1 > num2:
        print("num1 is greater than num2")
    elif num1 < num2:
        print("num1 is less than num2")
    elif num1 == num2:
        print("num1 is equal to num2")

        # get users' choice if Y or N
        restart = input("Do you want to restart? Y/N ")
        if restart == "Y" or restart == 'y':
            main()
        else:
            exit()

main()
