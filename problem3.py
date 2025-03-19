def sum_of_digits(n: int) -> int:
    return sum(int(digit) for digit in str(n))


print(sum_of_digits(1234))  
