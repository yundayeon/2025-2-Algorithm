#11월 14일

#%%
from lorem_text import lorem

lorem_text = lorem.sentence()
print(lorem_text)
print(lorem.paragraph())
for _ in range(5):
    print(lorem.sentence())
    
for _ in range(3):
    print(lorem.paragraph())
    print()

#%%

from faker import Faker
import random
fake = Faker()

print(fake.sentence())
print(fake.text)
print(fake.paragraph())

for _ in range(5):
    print(fake.sentence())
    
for _ in range(3):
    print(fake.paragraph())
    print()
    
fake = Faker('ko_KR')
people = []

for _ in range(5):
    person = {
        '이름': fake.name(),
        '주소': fake.address(),
        'email': fake.email(),
        'phone_number': fake.phone_number(),
        'birth_date': fake.date_of_birth().isoformat(),
        'company': fake.company(),
        'job': fake.job()
    }
    people.append(person)
    
for person in people:
    print(person)

# print("이름:", fake.name())
# print("주소:", fake.address())
# print("이메일", fake.email())    
# pNumber = f"010-{random.randint(1000,9999)}-{random.randint(1000,9999)}"
# print("맞춤 전화번호:", pNumber)

# %%
