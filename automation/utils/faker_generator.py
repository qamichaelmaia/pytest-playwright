from faker import Faker

faker = Faker()

def generate_user_data():
    return {
        "name": faker.name(),
        "email": faker.email(),
        "password": faker.password(),
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "company": faker.company(),
        "address": faker.address().replace("\n", ", "),
        "country": "Canada",
        "state": "Alberta",  
        "city": faker.city(),
        "zipcode": faker.zipcode(),
        "phone": faker.phone_number(),
    }
