fib_numbers = [0, 1]

for _ in range(48):
    next_number = fib_numbers[-1] + fib_numbers[-2]
    fib_numbers.append(next_number)

total_sum = sum(fib_numbers)

print(f"9. Sum of the first 50 fibonacci numbers: {total_sum}")