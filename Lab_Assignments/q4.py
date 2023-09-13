import sys

def is_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]

if len(sys.argv) < 2:
    print("Usage: python script.py number1 number2 ... numberN")
    sys.exit(1)
    
for arg in sys.argv[1:]:
    num = int(arg)
    if is_palindrome(num):
        print(f"{num} is a palindrome.")
    