import csv
import string
import random

SUBSITUTION_SAVE_FILE = './substitution.csv'

def read_encode():
    result = {}
    with open(SUBSITUTION_SAVE_FILE) as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            result[row[0]] = row[1]
    return result

def generate_random_substitution():
    results = list(string.ascii_lowercase)
    results.append(' ')
    random.shuffle(results)
    alphabet = list(string.ascii_lowercase)
    alphabet.append(' ')
    with open(SUBSITUTION_SAVE_FILE, 'w') as file:
        writer = csv.writer(file,delimiter=',')
        for tup in zip(alphabet, results):
            writer.writerow(tup)

def subs_cipher(to_encode):
    to_encode = to_encode.lower()
    cipher = read_encode()
    result = ''
    for c in to_encode:
        result = result + cipher[c]
    return result

def read_decode_substitution():
    cipher = read_encode()
    return {value: key for key, value in cipher.items()}

def decode_substitution(encoded, decode_map):
    result = ''
    for letter in encoded:
        result = result + decode_map[letter]
    return result

def decode_with_saved_substitution_cipher(encoded):
    decode_map = read_decode_substitution()
    return decode_substitution(encoded, decode_map)

def main():
    #generate_random_substitution()
    # subsitution encode and decode a message
    to_encode = 'a very secret message that you must not be deciphered'
    encoded = subs_cipher(to_encode)
    print("encoded = ", encoded)
    print("check decoded = ", decode_with_saved_substitution_cipher(encoded))

if __name__ == "__main__":
    main()
