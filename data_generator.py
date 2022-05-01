import random
import sys

import nacl.pwhash
from faker import Faker

Faker.seed(0)
random.seed(0)

fake = Faker()

num_of_users_to_generate = 100
password_dictionary_size = 100
password_in_dictionary_probability = 20

args_length = len(sys.argv)

if args_length > 1:
    num_of_users_to_generate = int(sys.argv[1])
if args_length > 2:
    password_dictionary_size = int(sys.argv[2])
if args_length > 3:
    password_in_dictionary_probability = int(sys.argv[3])

mocked_user_data = []

for i in range(0, num_of_users_to_generate):
    username = fake.bothify("user###")
    passwd = fake.password(length=12)
    hashed = nacl.pwhash.str(passwd.encode('utf-8')).decode('utf-8')
    mocked_user_data.append({"user": username, "passwd": passwd, "hash": hashed})

with open("user_hashes", "w") as user_hashes:
    user_hashes.writelines([x['user'] + " " + x['hash'] + "\n" for x in mocked_user_data])

with open("dictionary_with_matches", "w") as dict_with_match, open("dictionary_no_matches", "w") as dict_no_match:
    for i in range(0, password_dictionary_size):

        random_dictionary_entry = fake.password(length=12)

        if random.randint(0, 100) < password_in_dictionary_probability:
            matching_passwd = mocked_user_data[random.randint(0, num_of_users_to_generate-1)]['passwd']
            dict_with_match.write(matching_passwd + "\n")
            dict_no_match.write(random_dictionary_entry + "\n")
            continue

        dict_with_match.write(random_dictionary_entry + "\n")
        dict_no_match.write(random_dictionary_entry + "\n")

