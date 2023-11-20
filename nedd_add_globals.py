Var = 42
def ask_me():
     num = int(input("Enter number:"))
     return(num)

def add_global(num):
     return(num)


def main():
     global Var
     sum = ask_me()
     sum += ask_me()
     sum += add_global(Var)
     Var = sum
     print("sum:", sum)
     print("Global:", Var)

if __name__ == "__main__":
     main()
