# if 10 > 11:
#     print("entro en la condicional")

person = {
  "name": "Juan",
  "age": 20,
  "susbcription": False
}

person2 = {
    "name": "ale",
  "age": 22,
  "susbcription": True 
}

person3 = {
    "name": "gabriel",
  "age": 32,
  "susbcription": True 
}

users = [person, person2, person3]

# if person["susbcription"] == True:
#     print("puedes ver el contenido")

for i in users:
    if i["susbcription"] == True:
      name = i["name"]
      print(f"{name} puedes ver el contenido")


# 1 => lunes
# 2 => martes

day_number = int(input("dime un numero: "))

# if day_number == 1:
#   print("Lunes")
# if day_number == 2:
#   print("Martes")
# if day_number == 3:
#   print("Miercoles")
# if day_number == 4:
#   print("Jueves")


if day_number == 1:
  print("Lunes")
elif day_number == 2:
  print("Martes")
elif day_number == 3:
  print("Miercoles")
elif day_number == 4:
  print("Jueves")
else:
  print("puede ser viernes, sabado o domingo")

name = "hhh"
if name == "ana":
  print("te llamas ana")
else:
  print("nose como te llamas")







