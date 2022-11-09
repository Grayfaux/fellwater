import random
import string



# generates a random lookup table from all sets of punctuation, digits, ascii_letters and whitespace.
def generate_permutation(permutation_length):

    if permutation_length < 16:
        raise ValueError("permutation length must be 16 or greater")
    permutation = {}
    for letter in string.printable:

        permutation[letter] = ""
        for i in range(permutation_length):
            permutation[letter] += str(random.randint(0,1))
    if check_permutation_for_duplicates(permutation):
        return generate_permutation(permutation_length)
    return permutation


# generates a random lookup table from a string or list data passed in
# useful for cases where you don't need a predefined lookup table
def generate_permutation_session(input_data, permutation_length):

    if type(input_data) == list:
        input_data = ''.join(input_data)

    if permutation_length < 16:
        raise ValueError("permutation length must be 16 or greater")
    permutation = {}
    for letter in input_data:
        if letter in permutation:
            pass
        else:
            permutation[letter] = ""
            for i in range(permutation_length):
                permutation[letter] += str(random.randint(0, 1))
    if check_permutation_for_duplicates(permutation):
        return generate_permutation_session(input_data, permutation_length, )
    return permutation


# checks permutation_dict for duplicates and returns true or false.
# used inside all permutation generators
def check_permutation_for_duplicates(permutation_dict):

    for letter in permutation_dict:
        for letter2 in permutation_dict:
            if letter != letter2 and permutation_dict[letter] == permutation_dict[letter2]:
                return True
    return False


# encrypts plaintext using permutation_dict
def encrypt(input_string, permutation_dict):

    ciphertext = ""
    for letter in input_string:
        ciphertext += permutation_dict[letter]
    return ciphertext

# Take in ciphertext, permutation_dict and permutation_length, slices ciphertext into chunks of length
# permutation_length and decrypts it
def decrypt(ciphertext, permutation_dict, permutation_length):

    plaintext = ""
    for i in range(0, len(ciphertext), permutation_length):
        for letter in permutation_dict:
            if permutation_dict[letter] == ciphertext[i:i+permutation_length]:
                plaintext += letter
    return plaintext


# makes two lists. shuffles the index list
# take the input_string_list and create a new list with the characters in the order of the shuffled index list
def scramble_string_input(input_string):

    input_string_list = list(input_string)
    scrambled_index_list = list(range(len(input_string_list)))

    random.shuffle(scrambled_index_list)

    scrambled_string_list = []
    for i in range(len(input_string_list)):
        scrambled_string_list.append(input_string_list[scrambled_index_list[i]])
    scrambled_string = ''.join(scrambled_string_list)

    return scrambled_string, scrambled_index_list


# takes in a scrambled string and an index list and returns the original string
def unscramble_string_input(scrambled_string, index_list):

    scrambled_string_list = list(scrambled_string)
    original_string_list = [None] * len(scrambled_string_list)
    for i in range(len(scrambled_string_list)):
        original_string_list[index_list[i]] = scrambled_string_list[i]
    original_string = ''.join(original_string_list)
    return original_string


def easy_encrypt(input_string, permutation_length):
    permutation_dict = generate_permutation(permutation_length)
    scrambled_string, scrambled_index_list = scramble_string_input(input_string)
    ciphertext = encrypt(scrambled_string, permutation_dict)
    return permutation_dict, ciphertext, scrambled_index_list


def easy_decrypt(permutation_dict, ciphertext, scrambled_index_list, permutation_length):
    decrypted_string = decrypt(ciphertext, permutation_dict, permutation_length)
    original_string = unscramble_string_input(decrypted_string, scrambled_index_list)
    return original_string


def read_and_join_file(file_name):
    with open(file_name, 'r') as file:
        input_string = ""
        for line in file:
            input_string += line

    return input_string


# Example usage round trip

# input_data = "This is an example of data to encrypt."
#
# x = generate_permutation_session(input_data, 16)
# xx = scramble_string_input(input_data)
# y = encrypt(xx[0], x)
#
# z = decrypt(y, x, 16)
# zz = unscramble_string_input(z, xx[1])
# print(zz)

