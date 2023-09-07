#Mengganti pola pada sebuah string
import re

text = "Hello, World!"
new_text = re.sub("Hello", "Hi", text)

print(new_text)

#Output: Hi, World

