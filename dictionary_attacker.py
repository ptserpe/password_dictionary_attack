import sys
import time

import nacl.pwhash

with open(sys.argv[1], "r") as user_hashes:
    user_hashes_dict = [{'user': x.split(" ")[0], 'hash': x.split(" ")[1].replace("\n", "")} for x in user_hashes]

if user_hashes_dict is None:
    raise Exception('')

total_users = len(user_hashes_dict)
total_passwords_found = 0

with open(sys.argv[2], "r") as dictionary:
    passwd_dictionary = [x.replace("\n", "") for x in dictionary]

start_time = time.time()
n_users_attacked = 0
n_passwords_tested = 0

with open("found_passwords", "w") as found_passwords:
    for user in user_hashes_dict:

        for passwd in passwd_dictionary:
            passwd = passwd.replace("\n", "")

            try:
                res = nacl.pwhash.verify(user['hash'].encode('utf-8'), passwd.encode('utf-8'))
                print(f"The password of user \"{user['user']}\" is \"{passwd}\"")
                found_passwords.write(f"{passwd} {user['user']}\n")
                total_passwords_found += 1
            except:
                continue
            finally:
                n_passwords_tested += 1
                time_diff = time.time() - start_time
                if time_diff > 60:
                    print(f"tested {n_users_attacked} users and {n_passwords_tested} passwords in {time_diff} sec")
                    n_users_attacked = 0
                    n_passwords_tested = 0
                    start_time = time.time()

        n_users_attacked += 1

print(f"found the password of {total_passwords_found}/{len(user_hashes_dict)}")
