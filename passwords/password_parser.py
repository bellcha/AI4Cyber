import re

with open("rockyou.txt", "r") as f:
    words = f.read().splitlines()


with open("password_parse.csv", "w") as p:
    p.write(
        "password\tpassword_length\tnum_of_upper\tnum_of_lower\tnum_of_numbers\tnum_of_special\n"
    )
    for word in words:

        lenght = len(word)
        upper = len(re.findall(r"[A-Z]", word))
        lower = len(re.findall(r"[a-z]", word))
        number = len(re.findall(r"[0-9]", word))
        special = len(re.findall(r"[^A-Za-z0-9]", word))

        p.write(f"{word}\t{lenght}\t{upper}\t{lower}\t{number}\t{special}\n")

print("Done!")
