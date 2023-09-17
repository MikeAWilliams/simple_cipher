import csv
import string
import random


def read_english_words():
    with open('./english_words.txt') as file:
        return file.read().splitlines()


def count_words_in_list(words, word_list):
    result = 0
    for word in words:
        if word in word_list:
            result = result + 1
    return result


def rotate_letter(letter, shift):
    i = ord(letter)
    shifted = i - shift
    while shifted < 97: #97 is a
        shifted = shifted + 26     
    while shifted > 122: #122 is z
        shifted = shifted - 26
    return chr(shifted)

def decode_rotation(to_decode, shift):
    result = ''
    for letter in to_decode:
        if ' ' == letter:
            result = result + ' '
            continue
        result = result + rotate_letter(letter, shift)
    return result

def decode_rotation_brute(to_decode):
    word_list = read_english_words()
    best_solution = ''
    best_count = 0
    best_shift = 0
    for shift in range(-26, 27):
        potential_solution = decode_rotation(to_decode, shift)
        words_found = count_words_in_list(potential_solution.split(), word_list)
        if words_found > best_count:
            best_solution = potential_solution
            best_count = words_found
            best_shift = shift

    return best_shift, best_solution

def main():
    """
    # code to brute force decode a rotation cypher

    to_decode = 'lxmn vdbc kn uxwp jwm qjam cx pdnbb' #shifted by 87
    #to_decode = 'bncd ltrs ad knmf zmc gzqc sn ftdrr' # shifted  
    #to_decode = 'y myix oek bksa mxud oek jho je tusetu jxyi yj yi huqbbo bedw qdeoydw qdt xqi q xqht ixyvj yji qbie qd qdeoydw fxhqiu rusqiku yj yi ie bedw jxyi fqhj yi je wuj fqij jxu seccud meht oek qhu qjhqsjut je nobqfxedui qdt xqt ehqb iun myjx q mxqbu'
    shift, result = decode_rotation_brute(to_decode)
    print(shift, ' ', result)
    """

    #"""
    # rotation encode a message

    to_encode = 'congradulations you figured out the cypher'
    encoded = decode_rotation(to_encode, 15)
    print(encoded)
    check_decode = decode_rotation(encoded, -15)
    print(check_decode)
    #"""

if __name__ == "__main__":
    main()
