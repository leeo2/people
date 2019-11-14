# 11-13-19

from person import Person

new_person = Person("Jane", "Doe", "18", "brown", "blue")
print(new_person.description())
print(new_person.birthday())

print("~" * 30)

new_person2 = Person("John", "Doe", "20", "blond", "brown")
print(new_person2.description())
print(new_person2.birthday())
