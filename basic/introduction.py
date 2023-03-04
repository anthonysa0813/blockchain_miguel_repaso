# variables 

age = 12
name = "John"

countries = ["estados unidos", "peru", "ecuador"] # listas si son mutables

another_list = [1,True, "something"]
print(another_list)

# tuplas
students = ("jose", "ana", "pepe")
# las tuplas no son mutables
print(students)

# diccionario
product = {
    "name": "Laptop lenovo legion",
    "price": 6000,
    "characters": {
      "memory": "1TB",
      "ram": "16GB",
      "video": "NVIDIA RTX"
    }
}

# print(product)
# print(product["name"])
# print(product["characters"])
print(product["characters"]["ram"])