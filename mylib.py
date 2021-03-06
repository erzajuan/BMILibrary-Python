def BMI(x, y):
    y = y/100
    BMI = x/(y*y)
    print("BMI anda adalah  : {:.2f}".format(BMI))
    if BMI < 18.5:
        print("Anda Termasuk Kekurangan Berat badan")
    elif 25 > BMI >= 18.5:
        print("Anda Termasuk Normal")
    elif 30 > BMI >= 25:
        print("Anda Termasuk Kelebihan Berat Badan")
    else:
        print("Anda Termasuk Obesistas")
