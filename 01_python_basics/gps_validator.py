lalitude = int (input ("Введіть значення широти "))
longitude = int (input ("Введіть значення довготи"))

if (lalitude >=-90 and lalitude <=90) and (longitude >=-180 and longitude <=180):
    print ("GPS координати коректні.")

else:
    print("GPS координати некоректні.")