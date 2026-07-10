number = int (input("Введіть число "))
count = 0

while number != 0:
    if number > 5:
        count = count + 1
    number = int (input("Введіть число "))

print (count)
    