from faker import Faker
fake = Faker('zh_CN')
print(fake.address())
print(fake.name())
print(fake.phone_number())