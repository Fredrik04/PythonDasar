#3.	Mengambil bagian dari sebuah string yang cocok dengan pola tertentu
import re
text = "My Phone number is 123-456-7890"
match = re.search(r'\d{3}-\d{3}-\d{4}', text)

if match:
    print(match.group())

    