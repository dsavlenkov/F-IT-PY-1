src = not False and True or False and not True

src = True and True or False and False   # not False = True; not True = False

src = True or False  # True and True = True ; False and False = False

src = True  # True and False = True

result = True  # TODO подставить результат выражения

print(src == result)
