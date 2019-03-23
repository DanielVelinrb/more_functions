import random

def game_craps():
    craps_list = [2, 3, 12]
    natural_list = [7, 11]
    win_number = 0

    for _ in range(10000):
        r1 = random.randrange(1,6) 
        r2 = random.randrange(1,6)
        
        summatory = r1 + r2

        if summatory in natural_list:
            win_number += 1
            craps_list = [2, 3, 12]
            natural_list = [7, 11]
        elif summatory in craps_list:
            craps_list = [2, 3, 12]
            natural_list = [7, 11]
        else:
            natural_list = [summatory]
            craps_list = [7]
    print(f"The number of winning games is {win_number}")

def main():
    game_craps()
    

if __name__ == "__main__":
    main()
