def meal_test(answer):
     if answer == 1:
           print ("Fried Chicken Yummy!")
     elif answer == 2:
           print ("Burgers are cool")
     elif answer == 3:
           print ("Pizza be slapping sometimes")
     else:
           print ("That is not an option!")

def main():
     print ("Which is your favorite meal?")
     print ("1.Chicken")
     print ("2.Burger")
     print ("3.Pizza")
     answer = int (input())
     meal_test(answer)

if __name__ == "__main__":
     main()
