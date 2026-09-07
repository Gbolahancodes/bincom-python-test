input_sequence = "0101101011101011011101101000111"
output_sequence = ""
consecutive_ones = 0

for char in input_sequence:
    if char == '1':
        consecutive_ones += 1
        if consecutive_ones == 3:
            output_sequence += '1'
            consecutive_ones = 0
        else:
            output_sequence += '0'
    else:
        consecutive_ones = 0
        output_sequence += '0'

print(f"Input:  {input_sequence}")
print(f"Output: {output_sequence}")