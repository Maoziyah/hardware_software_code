# https://github.com/Maoziyah/hardware_software_code
# This is the first question and the menu of the code
def main ():
    print ("This program converts decimal numbers to binary and vise versa")
    userSelection = int (input("Choose your option: \n (1) binary to decimal \n (2) decimal to binary \n (3) close program"))
#This is the binary to decimal option
    if userSelection == 1:

        b_num = list(input("Input a binary number: "))
        value = 0

        for i in range(len(b_num)):
            digit = b_num.pop()
            if digit == '1':
                value = value + pow(2, i)
        print("The decimal value of the number is", value)
#This is the decimal to binary option
    elif userSelection == 2:

        def convertToBinary(n):
            if n > 1:
                convertToBinary(n//2)
            print(n % 2,end = '')

        dec = int (input("enter decimal number:"))

        convertToBinary(dec)
        print()
# This is the code to quit the program
    elif userSelection == 3:
        quit()
#This is when you dont pick a number between 1 and 3
    else:
        print ("pick a valid number")

if __name__ == "__main__":
     main()
