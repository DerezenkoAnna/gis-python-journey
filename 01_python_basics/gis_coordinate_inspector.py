latitude = int(input("Введіть значення широти "))
longitude = int (input ("Введіть значення довготи "))

if (latitude >=-90 and latitude <=90) and (longitude >=-180 and longitude <=180):
    print ("✅ GPS координати коректні.")

    if latitude >0:
        print ("Північна півкуля")

    if latitude <0:
        print ("Південна півкуля")

    if latitude ==0:
        print ("Екватор")

    if longitude >0:
        print ("Східна півкуля")

    if longitude <0:
        print ("Західна півкуля")

    if longitude ==0:
        print ("Нульовий меридіан")

else:
    print ("❌ GPS координати некоректні.")