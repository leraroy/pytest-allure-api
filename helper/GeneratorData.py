import random

from faker import Faker

fake = Faker()
class GeneratorData:

    def __init__(self):
        self.name = fake.first_name()
        self.due_date = fake.random_int(max=99999)
        self.description = fake.word()
        self.color = fake.color_name()
        self.priority = fake.random_int(min=1, max=4)

