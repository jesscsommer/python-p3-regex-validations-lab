import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"^[A-Z][-'A-z]+( [-'A-z]+)*$"
name_regex = re.compile(name)

phone_number = r"([(][1-9][0-9]{2}[)][ ][0-9]{3}[-][0-9]{4})|([1-9][0-9]{9})|([1-9][0-9]{2}[-][0-9]{3}[-][0-9]{4})"
phone_regex = re.compile(phone_number)

email_address = r"^[^0-9^\W][\w.]+[@][\w.]+"
email_regex = re.compile(email_address)
