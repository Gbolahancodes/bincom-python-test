#Question 8

import random

binary_number = "".join(random.choice(['0', '1']) for _ in range(4))

base_10_value = int(binary_number, 2)

print(f"Random binary number: {binary_number}")
print(f"8.Convert to base 10: {base_10_value}")