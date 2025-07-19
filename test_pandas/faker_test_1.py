from faker import Faker
import pandas as pd

fake = Faker('ru_RU')

# print(fake.name())
# print(fake.phone_number())
# print(fake.address())
# print(fake.msisdn())
# print(fake.company())
# print(fake.date_of_birth())

data = [{
    "name": fake.name(),
    "email": fake.email(),
    "address": fake.address(),
    "country": fake.country(),
    "phone": fake.phone_number(),
    "date_of_birth": fake.date_of_birth(),
    "pass_number": fake.passport_number(),
    "company": fake.company(),
    "ip_address": fake.ipv4()
} for _ in range (100)]

df = pd.DataFrame(data)
df.to_excel('Тест_faker.xlsx', index=False)




# data_2 = {
#     "Россия"
# }