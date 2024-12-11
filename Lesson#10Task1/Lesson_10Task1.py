pets = {
    'Имя питомца: ':{}}
pet_name = str(input("Введите имя питомца: "))
pet_type = str(input("Введите вид питомца: "))
pet_age = int(input("Введите возраст питомца: "))
owner_name = str(input("Введите имя владелца: "))

pets[pet_name] = {}
pets[pet_name]['Вид питомца:'] = pet_type
pets[pet_name]['Возраст питомца:'] = pet_age
pets[pet_name]['Имя владельца'] = owner_name

print(pets)