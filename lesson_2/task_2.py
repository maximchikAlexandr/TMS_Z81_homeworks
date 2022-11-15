input_str = 'AAAABBBBCCCCDDDDFFFF'
count_steps = int(len(input_str) / 4)
s1, s2, s3, s4, s5 = [input_str[i * 4: i * 4 + 4] for i in range(count_steps)]
output_str = s1 + s2 + s3 + s4 + s5
print(output_str)
print(input_str == output_str)
