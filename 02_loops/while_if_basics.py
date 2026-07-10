area = int (input ("Введіть площу ділянки "))
count = 0

while area != 0:
    if area >1000:
        count = count + 1

    area = int (input ("Введіть площу ділянки "))
print ("Загальна кількість ділянок становить", count)