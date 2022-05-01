# Project 1

## Files Description
- data_generator.py : program that generates passwards and stores the password hashesin "user_hashes" file. It also generates both dictionary_with_matches and dictionary_no_matches files for validation purposes. 

Usage: 
```
python3 ./data_generator.py users_num passwords_num probability
```

- users_num: the number of users to generate [int]
- passords_num: the number of passwords to generate [int]
- probability: the probability of generated passwords containing an actual user password [int - default: 20]

Example:
```
python3 ./data_generator.py 10 10 40
```

- dictionary_attacker.py: A program that uses two inputs:

    - The file created by the first program (user_hashes)

    - A file with popular passwords (dictionary_with_macthes)

It finds all the passwords (if any) from B that appear in A and return a file(found_passwords) with the password and the corresponding username.

Example:
```
python3 ./attacker.py user_hashes dictionary_with_matches
```