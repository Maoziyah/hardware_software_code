Var = 42

def add(num):
     return(num + Var )


def main():
     user1= int(input("input first number"))
     user2= int(input("input second number"))
     total= user1 + user2
     number= add (total)
     print("Sum:", number)
     print("Global:", Var)

if __name__ == "__main__":
    main()
