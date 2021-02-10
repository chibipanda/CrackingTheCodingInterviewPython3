
# IsUnique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use
# additional data structures?
def is_unique(input_string):
    chars = {}
    for i in input_string:
        chars[i] = 0
    for i in input_string:
        chars[i] += 1
    for i in input_string:
        if chars[i] > 1:
            return False
    return True

# checkPermutation: Given two strings, write a method to decide if one is permutation of the other
def is_permutation(input_string_1, input_string_2):
    # Assumption here is that the comparison is case sensitive.
    chars_1 = {}
    chars_2 = {}
    for i in input_string_1:
        chars_1[i] = 0
    for i in input_string_2:
        chars_2[i] = 0
    for i in input_string_1:
        chars_1[i] += 1
    for i in input_string_2:
        chars_2[i] += 1
    if chars_1 == chars_2:
        return True
    else:
        return False

# URLify
def urlify(string_input, length):
    new_string = list(string_input)
    new_string_index = 0
    for i in range(length):
        if string_input[i] == ' ':
            new_string[new_string_index] = '%'
            new_string[new_string_index + 1] = '2'
            new_string[new_string_index + 2] = '0'
            new_string_index += 3
        else:
            new_string[new_string_index] = string_input[i]
            new_string_index += 1
    return new_string

def urlify_in_place(string_input, length):
    new_string = list(string_input)
    char_being_worked_on = length - 1
    i = len(new_string) - 1
    while i >= 0:
        if new_string[char_being_worked_on] == ' ':
            new_string[i] = '0'
            new_string[i - 1] = '2'
            new_string[i - 2] = '%'
            i -= 3
            char_being_worked_on -= 1
        else:
            new_string[i] = new_string[char_being_worked_on]
            i -= 1
            char_being_worked_on -= 1
    return new_string

# PalindromePermutation
def palindrome_permutation(string_input):
    string_input_processed = string_input.lower()
    chars = {}
    for i in string_input_processed:
        if i == ' ':
            continue
        chars[i] = 0
    for i in string_input_processed:
        if i == ' ':
            continue
        chars[i] += 1
    number_of_odd_character = 0
    for i in string_input_processed:
        if i == ' ':
            continue
        if chars[i] % 2 == 1:
            number_of_odd_character += 1
    if number_of_odd_character < 2:
        return True
    else:
        return False

# OneAway
def one_away(input_string_1, input_string_2):
    # if it's the same string, return true
    if input_string_1 == input_string_2:
        return True
    if abs(len(input_string_2) - len(input_string_1)) > 1:
        return False
    # if the length is not the same, make sure that there's only 1 letter
    # difference
    shorter_string = input_string_1
    longer_string = input_string_2
    if len(input_string_1) > len(input_string_2):
        shorter_string = input_string_2
        longer_string = input_string_1
    if len(longer_string) - len(shorter_string) > 0:
        longer_string_index = 0
        shorter_string_index = 0
        while longer_string_index < len(longer_string) and shorter_string_index < len(shorter_string):
            if longer_string[longer_string_index] != shorter_string[shorter_string_index]:
                if longer_string_index != shorter_string_index:
                    return False
                longer_string_index += 1
            else:
                longer_string_index += 1
                shorter_string_index += 1
    # if the length is the same, needs to make sure that there's only one difference
    if len(input_string_1) == len(input_string_2):
        number_of_different_chars = 0
        for i in range(len(input_string_1)):
            if input_string_1[i] != input_string_2[i]:
                number_of_different_chars += 1
            if number_of_different_chars > 1:
                return False
    return True

# StringCompression
def string_compression(input_string):
    minimum_length = len(input_string)
    current_index = 0
    new_string = input_string[0]
    number_of_repeats = 1
    while current_index < len(input_string) - 1:
        if len(new_string) >= minimum_length:
            return input_string
        if input_string[current_index + 1] == input_string[current_index]:
            number_of_repeats += 1
            current_index += 1
        else:
            new_string += str(number_of_repeats)
            number_of_repeats = 1
            current_index += 1
            new_string += input_string[current_index]
    new_string += str(number_of_repeats)
    if len(new_string) >= minimum_length:
        return input_string
    return new_string

# RotateMatrix
# Mod = rotate a matrix of some object 90 degrees
def rotate_matrix(matrix):
    pass

# ZeroMatrix
def zero_matrix(matrix):
    new_matrix = matrix.copy()
    zero_columns = []
    for i in matrix:
        for j in i:
            if j == 0:
                zero_columns.append(i.index(j))
                new_matrix[new_matrix.index(i)] = [0] * len(i)
    for i in range(len(new_matrix)):
        for j in zero_columns:
            new_matrix[i][j] = 0
    return new_matrix

# String Rotation
def is_substring(word_is_substring, full_word):
    pass

def stringRotation():
    pass
