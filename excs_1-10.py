import re
from auto_test import AutoTests
# Exercices from https://www.w3resource.com/python-exercises/re/


# 1. Write a Python program to check that a string contains only a certain set of characters
# (in this case a-z, A-Z and 0-9).
def match_str(_str):
    pattern = re.compile(r'[a-zA-Z0-9]+')
    # pattern = re.compile(r'[\d\w]+')  # Considering that need accent on the words and also can use some special carct
    # like '_'
    match = re.search(pattern, _str)
    print(match)
    print(match.group())
    return match.group() is _str


# 2. Write a Python program that matches a string that has an a followed by zero or more b's.
def match_str2(_str):
    pattern = re.compile(r'ab*')
    match = re.search(pattern, _str)
    if match:
        # print(match)
        # print(match.group())
        pass
    return match is not None


# 3. Write a Python program that matches a string that has an a followed by one or more b's.
def match_str3(_str):
    pattern = re.compile(r'ab+')
    match = re.search(pattern, _str)
    if match:
        # print(match)
        # print(match.group())
        pass
    return match is not None


#  4. Write a Python program that matches a string that has an a followed by zero or one 'b'.
def match_str4(_str):
    pattern = re.compile(r'ab*')
    matches = re.findall(pattern, _str)
    if not matches:
        return False
    return all(match == 'a' or match == 'b' for match in matches)


# 5. Write a Python program that matches a string that has an a followed by three 'b'.
def match_str5(_str):
    pattern = re.compile(r'abbb')
    match = re.search(pattern, _str)
    if match:
        # print(match)
        # print(match.group())
        pass
    return True if match is not None else False


# 6. Write a Python program that matches a string that has an a followed by two to three 'b'.
def match_str6(_str):
    pattern = re.compile(r'ab{2,3}')
    match = re.search(pattern, _str)
    if match:
        # print(match)
        # print(match.group())
        pass
    return match is not None


# 7. Write a Python program to find sequences of lowercase letters joined by an underscore.
def match_str7(_str):
    pattern = re.compile(r'[a-z]+_')
    match = re.findall(pattern, _str)
    print(match)
    return match


# 8. Write a Python program to find the sequences of one upper case letter followed by lower case letters.
def match_str8(_str):
    pattern = re.compile(r'[A-Z][a-z]+')
    match = re.findall(pattern, _str)
    print(match)
    return match


# 9. Write a Python program that matches a string that has an 'a' followed by anything ending in 'b'.
def match_str9(_str):
    pattern = re.compile(r'a.+?b')
    match = re.findall(pattern, _str)
    print(match)
    return match


# 10.Write a Python program that matches a word at the beginning of a string.
def match_str10(_str):
    pattern = re.compile(r'^[A-Za-z][a-z]+\b')
    match = re.findall(pattern, _str)
    return match


if __name__ == "__main__":
    # Obs.: All exercises were done considering case sensitivity as True
    test = AutoTests.test_reg_ex_funcs  # Initialize the test class
    test_func = 10  # Change this value for decide what funct you pretend to test.
    print(f'Actual test func num:{test_func} \n')

    # Auto Tests f_1 - Just return True if the input str is [A-Za-z0-9]
    if test_func == 1:
        test(match_str, 'Aabcd123', True)
        test(match_str, 'abcd123_', False)
        test(match_str, 'abcd123*()', False)

    # Auto Tests for f_2 - Since it's 0 or more 'b', just by having an 'a' the test return true.
    elif test_func == 2:
        test(match_str2, 'acd123', True)
        test(match_str2, 'Acd123', False)
        test(match_str2, 'cd12abb3', True)

    # Auto Tests for f_3 - Must be one or more 'b' after an 'a' for return True.
    elif test_func == 3:
        test(match_str3, 'acd123', False)
        test(match_str3, 'Abcd123', False)
        test(match_str3, 'cd12abb3', True)

    # Auto Tests for f_4 - Return True if has an 'a' followed by zero or one 'b' not more than 1 'b'.
    elif test_func == 4:
        test(match_str4, 'acd123', True)
        test(match_str4, 'Abcd123', False)
        test(match_str4, 'cd12abb3', False)

    # Auto Tests for f_5 - Return True just if has an 'a' followed by 3 'b'.
    elif test_func == 5:
        test(match_str5, 'abbbcd123', True)
        test(match_str5, 'Abbbcd123', False)
        test(match_str5, 'cd12abb3', False)

    # Auto Tests for f_6 - Return True just if has an 'a' followed by 2 to 3 'b'.
    elif test_func == 6:
        test(match_str6, 'abbcd123', True)
        test(match_str6, 'abbbcd123', True)
        test(match_str6, 'cd12Abb3', False)
        test(match_str6, 'cd12ab3', False)

    # Auto Tests for f_7 - find sequences of lowercase letters joined by an underscore.
    elif test_func == 7:
        test(match_str7, 'abb_cd123', ['abb_'])
        test(match_str7, 'a_bbbc_d123_ aaaxy12b_', ['a_', 'bbbc_', 'b_'])
        test(match_str7, 'abB_cdD123J ', [])

    # Auto Tests for f_8 - find the sequences of one upper case letter followed by lower case letters.
    elif test_func == 8:
        test(match_str8, 'Abb_cd1Ax23', ['Abb', 'Ax'])
        test(match_str8, 'a_bBxc_d123_ aaaJxy12b_', ['Bxc', 'Jxy'])
        test(match_str8, 'abB_cd123', [])

    # Auto Tests for f_9 - match a string that has an 'a' followed by anything ending in 'b'.
    elif test_func == 9:
        test(match_str9, 'Abb_cd1Ax23', [])
        test(match_str9, 'a_bBxc_d123_ aaaJxy12b_', ['a_b', 'aaaJxy12b'])
        test(match_str9, r'abB_cd123a&*´´\/b', [r'abB_cd123a&*´´\/b'])

    # Auto Tests for f_10 - matches a word at the beginning of a string. The word could start with upper or
    # lower case, but must follow with just lower cases. Obs.: A letter is not considered a word.
    elif test_func == 10:
        test(match_str10, 'Abb_cd1Ax23', [])
        test(match_str10, 'ab _bBxc_d123_ aaaJxy12b_', ['ab'])
        test(match_str10, r'abB _cd123a&*´´\/b', [])
        test(match_str10, r'Abb _cd123a&*´´\/b', ['Abb'])
