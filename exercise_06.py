def get_prefix_and_size(n, d):
    boolean_confirmation = ""
    prefix_list = [4, 5, 37, 6]
    if d == 37:
        boolean_confirmation = True
    else:
        d = int(str(n)[0:1])
        if d in prefix_list:
            boolean_confirmation = True
        else:
            boolean_confirmation = False

        final_message = f"The number of digits of the credit car is {len(str(n))}.\\\
    {boolean_confirmation}, the credit car has a valid prefix."
    return final_message


def two_digits_to_one(n):
    n_list = list(str(n))
    return int(n_list[0]) + int(n_list[1])


def sum_couple_numbers(number):
    n_list = list(str(number))
    summatory =  0
    for i in range(len(n_list)):
        if i % 2 == 0:
            to_sum = int(n_list[i]) * 2
            if len(str(to_sum)) > 1:
                to_sum = two_digits_to_one(to_sum)
                summatory += to_sum
            else:
                summatory += to_sum
    return summatory


def sum_odd_numbers(number):
    n_list = list(str(number)[::-1])
    summatory = 0
    for i in range(len(n_list)):
        if i % 2 == 0:
            to_sum = int(n_list[i])
            summatory += to_sum
    return summatory
    

def validate_number(n):
    extension = len(str(n))
    d = int(str(n)[0:2])
    if extension < 13 or extension > 16:
        print("Invalid number")
    else:
        to_analize = sum_couple_numbers(n) + sum_odd_numbers(n)
        if to_analize % 10 != 0:
            print("Invalid number")
        else:
            print("Valid number")
    print(get_prefix_and_size(n, d))


def main():
    credit_card_number = int(eval(input("Enter your credit car number: ")))
    validate_number(credit_card_number)


if __name__ == "__main__":
    main()
