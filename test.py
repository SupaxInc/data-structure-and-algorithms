import re

s = "A man, a plan, a canal: Panama"

newString = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

print(newString)
print(newString[::-1])
print(newString[0:1])