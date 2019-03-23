import random

def game_craps():
    limit = 0
    craps_list = [2, 3, 12]
    natural_list = [7, 11]

    while limit < 2:
        r1 = random.randrange(1,6) 
        r2 = random.randrange(1,6)
        
        summatory = r1 + r2

        if summatory in natural_list:
            print(f"You rolled {r1} + {r2} = {summatory}\nYou win")
            limit = 2
        elif summatory in craps_list:
            print(f"You rolled {r1} + {r2} = {summatory}\nYou lose")
            limit = 2
        else:
            natural_list = [summatory]
            craps_list = [7]
            print(f"You rolled {r1} + {r2} = {summatory}\nPoint is {summatory}")


def main():
    game_craps()
    

if __name__ == "__main__":
    main()
