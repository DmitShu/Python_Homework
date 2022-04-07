# class User:
#     number_of_fingers = 5
#     number_of_eyes = 2
#
# peter = User()
# peter.name = "Peter Robertson"
#
# julia = User()
# julia.name = "Julia Donaldson"
#
# print(peter.name)
# print('\n')
# print(julia.name)
# print(julia.number_of_fingers)

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

peter = User(name="Peter Robertson", email="peterrobertson@mail.com")
julia = User(name="Julia Donaldson", email="juliadonaldson@mail.com")

print(peter.name)
print(julia.email)
