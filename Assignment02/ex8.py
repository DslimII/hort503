formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "David J Sliman II",
    "Is taking Hort503",
    "On Tuesday and Thursdays",
    "at 10:35 AM"
))