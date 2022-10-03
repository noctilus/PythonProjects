# Your program is to use the brute-force approach in order to find
# the Answer to Life, the Universe, and Everything. More precisely...
# rewrite small numbers from input to output. Stop processing input after
# reading in the number 42. All numbers at input are integers of one or two digits.

# Example

# Input:
# 1
# 2
# 88
# 42
# 99

# Output:
# 1
# 2
# 88
# input_numbers = (1, 2, 88, 42, 99)

# for i in input_numbers:
#     if i == 42:
#         break
#     print(i)


# print("The end")
def take_input():
    """Check if inputed no == 42"""
    input_number = int(input())

    if input_number == 42:
        exit()
    else:
        print(input_number)
    take_input()


take_input()
