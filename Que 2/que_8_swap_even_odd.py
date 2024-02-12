# 8.Write a program which swap every odd-even position character in the string. 
def swap_odd_even(input_str):
    chars = list(input_str)
    for i in range(1, len(chars), 2):  # Start from index 1 for odd positions
        chars[i], chars[i-1] = chars[i-1], chars[i]  # Swap odd-even positions
    return ''.join(chars)

user_input = input("Enter a string: ")
output_result = swap_odd_even(user_input)
print("Output:", output_result)
