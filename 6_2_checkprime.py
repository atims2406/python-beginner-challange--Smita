def is_prime(number):
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count = count + 1
    if count == 2:
        return True
    else:
        return False


number = int(input("Enter a number: "))

if is_prime(number):
    print("Prime number")
else:
    print("Not a prime number")