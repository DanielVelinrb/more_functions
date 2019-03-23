import random

def random_value():
    limits_list = [0, 1]
    random_value = random.choice(limits_list)
    return random_value


def print_matrix(n):
    for _ in range(n):
        to_print = ""
        for _ in range(n):
            to_print += f"{random_value():<2}"
        print(to_print)


def main():
    number = int(input("Enter n: "))
    print_matrix(number)


if __name__ == "__main__":
    main()
