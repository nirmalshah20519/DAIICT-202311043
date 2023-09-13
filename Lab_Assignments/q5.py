import re
input_string = "Hello world"
words = input_string.split()
camel_case_words = [words[0].lower()] + [word.capitalize() for word in words[1:]]
camel_case_string = ''.join(camel_case_words)
print(camel_case_string)