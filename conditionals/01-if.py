sueldo = int(input("dime tu sueldo, para calcular el impuesto: "))

# if sueldo < 1000:
#     print("El impuesto no se aplica a tu monto...")


# if sueldo > 1000:
#     calculate_discount = (10/100) * sueldo
#     print(calculate_discount)


# if sueldo < 1000:
#     print("El impuesto no se aplica a tu monto...")
# elif sueldo == 1000:
#     calculate_discount = (10/100) * sueldo
#     print(calculate_discount)
# elif sueldo > 1000:
#     calculate_discount = (10/100) * sueldo
#     print(calculate_discount)

# || significa or en otros lenguajes
# if = si  ||  elif = sino

if sueldo < 1000:
    print("El impuesto no se aplica a tu monto...")
elif sueldo == 1000 or sueldo > 1000:
    calculate_discount = (10/100) * sueldo
    print(calculate_discount)








