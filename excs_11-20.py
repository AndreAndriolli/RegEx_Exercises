import re
from auto_test import AutoTests
# Exercises from https://www.w3resource.com/python-exercises/re/


# 11. Write a Python program that matches a word at the end of a string, with optional punctuation
def match_str(_str):
    pattern = re.compile(r'(^|\s)[A-Za-z]+[.!?]*$')
    # pattern = re.compile(r' [A-Za-z]+[\W]{0,3}$')  # It ll consider a lot of carct. that may not be useful.
    match = re.search(pattern, _str)
    print(match)
    return match.group()[1:] if match is not None else False


# 12. Write a Python program that matches a word containing 'z'.
def match_str2(_str):
    pattern = re.compile(r'[A-Ya-y]*[Zz]+[A-Za-z]*')
    matches = re.findall(pattern, _str)
    print(matches)
    return matches if not None else False


# 13. Write a Python program that matches a word containing 'z', not in the start or end of the word.
def match_str3(_str):
    # 'z' word not in the start or in the end of str
    pattern = re.compile(r'[A-Ya-y]+[Zz]+[A-Za-z]*[A-Ya-y]+')
    matches = re.findall(pattern, _str)
    print(matches)
    return matches if not None else False


#  14. Write a Python program to match a string that contains only upper and lowercase letters,
#  numbers, and underscores.
def match_str4(_str):
    pattern = re.compile(r'\w+')
    matches = re.findall(pattern, _str)
    print(matches)
    return matches if matches else False


# 15. Write a Python program that starts each string with a specific number.
def match_str5(_str, num):
    pattern = re.compile(fr'\b{num}-\w*\b')
    matches = re.findall(pattern, _str)
    print(matches)
    return matches if matches else False


# 16. Write a Python program to remove leading zeros from an IP address.
def match_str6(ip_address):
    # pattern = re.compile(r'[1-9][0-9]?[0-9]?\.?')
    match = re.sub(r'\.0*', '.', ip_address)
    match2 = re.sub(r'\.\.', '.0.', match)
    match3 = re.sub(r'^0*', '', match2)
    match4 = re.sub(r'^\.', '0.', match3)
    match5 = re.sub(r'\.$', '.0', match4)
    print(match5)
    return match5


# 17. Write a Python program to check for a number at the end of a string.
def match_str7(_str, num_find):
    pattern = re.compile(fr'\b[A-Za-z0-9]*?{num_find}\b')
    matches = re.findall(pattern, _str)
    print(matches)
    return matches


# Write a Python program to search for numbers (0-9) of length between 1 and 3 in a given string.
# "Exercises number 1, 12, 13, and 345 are important"
def match_str8(_str):
    pattern = re.compile(r'\b[0-9]{1,3}\b')
    matches = re.findall(pattern, _str)
    print(matches)
    return matches


# 19. Write a Python program to search for literal strings within a string.
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox', 'dog', 'horse'
def match_str9(_str, word):
    pattern = re.compile(fr'\b{word}\b')
    matches = re.findall(pattern, _str)
    return matches if matches else False


# 20. Write a Python program to search for a literal string in a string
# and also find the location within the original string where the pattern occurs.
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox'
def match_str10(_str, word):
    pattern = re.compile(fr'\b{word}\b')
    matches = pattern.finditer(_str)
    spans = [match.span() for match in matches]
    print(spans)
    return spans


if __name__ == "__main__":
    # Obs.: All exercises were done considering case sensitivity as True
    test = AutoTests.test_reg_ex_funcs  # Initialize the test class
    test_func = 1  # Change this value for decide what funct you pretend to test.
    print(f'Actual test func num:{test_func} \n')

    # Auto Tests f_1 - matches a word at the end of a string, with optional punctuation.
    # I considered that every word start with a white space or a begging of string.
    if test_func == 1:
        test(match_str, 'Aabcd123 pass', 'pass')
        test(match_str, 'abcd123_ fun', 'fun')
        test(match_str, 'abcd123*()run', False)
        test(match_str, r'word abcd123*()_aa', False)

    # Auto Tests for f_2 - matches a word containing 'z'
    elif test_func == 2:
        test(match_str2, 'mouse Zebra sorry', ['Zebra'])
        test(match_str2, 'potato Fuzzy shoes quiz keyboard3', ['Fuzzy', 'quiz'])
        test(match_str2, 'Zonai over, call Zelda', ['Zonai', 'Zelda'])
        test(match_str2, 'aZzZBzZ', ['aZzZBzZ'])

    # Auto Tests for f_3 - matches a word containing 'z', not in the start or end of the word.
    elif test_func == 3:
        test(match_str3, 'mouse Zebra sorry', [])
        test(match_str3, 'potato Fuzzy shoes quiz keyboard3', ['Fuzzy'])
        test(match_str3, 'Zonai over, call Zelda', [])
        test(match_str3, 'aZzZBzX', ['aZzZBzX'])

    # Auto Tests for f_4 - match a string that contains only upper and lowercase letters,
    # numbers, and underscores.
    elif test_func == 4:
        test(match_str4, 'mouse3 Zebra sorry', ['mouse3', 'Zebra', 'sorry'])
        test(match_str4, 'potato_ Fuzzy shoes quiz keyboard3',
             ['potato_', 'Fuzzy', 'shoes', 'quiz', 'keyboard3'])
        test(match_str4, r'Zonai\ over*(), call Zelda', ['Zonai', 'over', 'call', 'Zelda'])
        test(match_str4, 'aZz1Z5Bz34X', ['aZz1Z5Bz34X'])

    # Auto Tests for f_5 - starts each string with a specific number.
    elif test_func == 5:
        test(match_str5, ['5-Zoom 2-mouse 1-Zebra 4-sorry 5-potato 2-Fuzzy', 2],
             ['2-mouse', '2-Fuzzy'])
        test(match_str5, ['5-Zoom 2-mouse 1-Zebra 4-sorry 5-potato 2-Fuzzy', 5],
             ['5-Zoom', '5-potato'])
        test(match_str5, ['5-Zoom 2-mouse 1-Zebra 4-sorry 5-potato 2-Fuzzy', 1], ['1-Zebra'])
        test(match_str5, ['5-Zoom 2-mouse 1-Zebra 4-sorry 5-potato 2-Fuzzy', 6], False)

    # Auto Tests for f_6 - remove leading zeros from an IP address.
    elif test_func == 6:
        test(match_str6, '002.068.000.001', '2.68.0.1')
        test(match_str6, '002.068.001.000', '2.68.1.0')
        test(match_str6, '000.068.001.002', '0.68.1.2')

    # Auto Tests for f_7 - check for a number at the end of a string.
    elif test_func == 7:
        test(match_str7, ['Zoom1 mouse1 Zebra2 sorry3 potato5 Fuzzy8 shoes13 quiz21 keyboard34 ', 1],
             ['Zoom1', 'mouse1', 'quiz21'])
        test(match_str7, ['Zoom1 mouse1 Zebra2 sorry3 potato5 Fuzzy8 shoes13 quiz21 keyboard34 ', 21],
             ['quiz21'])
        test(match_str7, ['Zoom1 mouse1 Zebra2 sorry3 potato5 Fuzzy8 shoes13 quiz21 keyboard34 ', 34],
             ['keyboard34'])

    # Auto Tests for f_8 - search for numbers (0-9) of length between 1 and 3 in a given string
    elif test_func == 8:
        test(match_str8, '1 12 13 345 5555 485 2 3 5',
             ['1', '12', '13', '345', '485', '2', '3', '5'])
        test(match_str8, '12 13 345 5555 485222 2 3 5',
             ['12', '13', '345', '2', '3', '5'])

    # Auto Tests for f_9 - search for literal strings within a string.
    elif test_func == 9:
        test(match_str9, ['The quick brown fox jumps over the lazy dog.', 'fox'],
             ['fox'])
        test(match_str9, ['The quick brown fox jumps over the lazy dog.', 'dog'],
             ['dog'])
        test(match_str9, ['The quick brown fox jumps over the lazy dog.', 'horse'],
             False)

    # Auto Tests for f_10 - search for a literal string in a string and also
    # find the location within the original string where the pattern occurs.
    elif test_func == 10:
        test(match_str10, ['The quick brown fox jumps over the lazy dog.', 'fox'],
             [(16, 19)])
        test(match_str10, ['The quick brown dog jumps over the other lazy dog.', 'dog'],
             [(16, 19), (46, 49)])
        test(match_str10, ['The quick brown fox jumps over the lazy dog.', 'horse'],
             [])
