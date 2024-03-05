from random import randint

def main():
    print("This is a guessing game")
    max = int(input("Enter max value you want: "))
    i = randint(0, max)
    run_game(i)

def run_game(i):
    print("\nEnter Ctrl+c to Exit")
    count = 0
    while True:
        try:
            x = input("Enter your Guess : ")
            count+=1
            x = int(x)
        except ValueError:
            print("Enter Valid Input")
            continue
        except KeyboardInterrupt:
            print("\nOky you have exited the Game")
            return
        else:
            if(x == i):
                 print(f"Great you have guess it correctly after {count} tries")
                 return
            elif(x > i):
                print("Ohh, its a larger number \nNo worries try again\n")
                continue
            else:
                print("Ohh, its a smaller number \nNo worries try again\n")
                continue

if __name__ == '__main__':
    main()

