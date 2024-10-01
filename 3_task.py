import re

def normalize_phone(phone_number):
 phone_number_list = re.findall(r"\d", phone_number) # "r" before "\d" because in VScode, have message about SyntaxWarning: invalid escape sequence '\d'
 phone_number_str = "".join(phone_number_list)
 search_pattern = r"(0\d{2})"
 separate_number = re.split(search_pattern, phone_number_str)
 
 return f"+38{ separate_number[1] }{  separate_number[2] }"

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)