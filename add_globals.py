Var = 42

def add(num1,num2):
    global Var
    Var +=(num1 + num2) + Var
    return Var

def main():
     num1 = int(input("Enter first number"))
     num2 = int(input("Enter first number"))

     number= add(num1,num2)

     print ("Updated Var",Var)

if __name__ == "__main__":
     main()
