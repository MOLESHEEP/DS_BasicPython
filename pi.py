from curses.ascii import isalpha
import string


text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO
count = 0
out = ""
for char in text:
    if char.isalpha():
        count = count + 1
    elif count!=0:
        out   = out + str(count)
        count = 0
    else:
        count = 0
print(out)
