def palindrome_number(number):
    if int(str(number)[::-1]) == number:
        return number


def determinate_primes_number(number):
    cont = 0
    for i in range(1, number):
        if number % i == 0:
            cont += 1
            if cont > 1:
                return None
    return number


def palindrome_prime(number):
    if number == palindrome_number(number):
        return number


def print_prime_numbers():
    prime_list = []
    limit = 0
    while len(prime_list) < 100: 
        to_eval = determinate_primes_number(limit)
        if 0 or 1 in prime_list:
            prime_list.remove(0)
            prime_list.remove(1)
        if to_eval != None:  
            if limit == palindrome_number(limit):
                prime_list.append(to_eval)
        limit += 1
    
    cont = 0
    for i in range(len(prime_list)):
        print(f"{prime_list[i]:>7}", end= "")
        cont += 1
        if cont == 10:
            print("\n")
            cont = 0
    

def main():
    print_prime_numbers()


if __name__ == "__main__":
    main()
