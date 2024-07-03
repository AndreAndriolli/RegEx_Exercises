import re
# Exercices from https://www.w3resource.com/python-exercises/re/

# Arquivo with changes for test github
# 1. Write a Python program to check that a string contains only a certain set of characters
# (in this case a-z, A-Z and 0-9).
def match_str(_str):
    pattern = re.compile(r'[a-zA-Z0-9]+')
    # pattern = re.compile(r'[\d\w]+')  # Considering that need accent on the words and also can use some special carct
    # like '_'
    match = re.search(pattern, _str)
    # print(match)
    # print(match.group())
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
    pattern = re.compile(r'ab?')
    match = re.search(pattern, _str)
    if match:
        # print(match)
        # print(match.group())
        pass
    return match is not None


# 5. Write a Python program that matches a string that has an a followed by three 'b'.
def match_str5(_str):
    pattern = re.compile(r'abbb')
    match = re.search(pattern, _str)
    if match:
        # print(match)
        # print(match.group())
        pass
    return match is not None


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
    pattern = re.compile(r'[a-z]*_')
    match = re.findall(pattern, _str)
    return match


# 8. Write a Python program to find the sequences of one upper case letter followed by lower case letters.
def match_str8(_str):
    pattern = re.compile(r'[A-Z][a-z]+')
    match = re.findall(pattern, _str)
    return match


# 9. Write a Python program that matches a string that has an 'a' followed by anything ending in 'b'.
def match_str9(_str):
    pattern = re.compile(r'a.+?b')
    match = re.findall(pattern, _str)
    return True if match else False


# 10.Write a Python program that matches a word at the beginning of a string.
def match_str10(_str):
    pattern = re.compile(r'^[A-Za-z]+ ')
    match = re.search(pattern, _str)
    if match:
        # print(match)
        # print(match.group())
        pass
    return match.group() if match else False


if __name__ == "__main__":
    # print(match_str('abcd123'))  # 1
    # print(match_str2('a2adfav89324abfsgfd'))  # 2
    # print(match_str3('a2adfav89324afsgfd'))  # 3
    # print(match_str4('ab2adfav89324afsgfd'))  # 4
    # print(match_str5('abb2adfav89324abbbfsgfd'))  # 5
    # print(match_str6('abb2adfav89324abbbfsgfd'))  # 6
    # print(match_str7('abb2adf_av89324abbbfsgfd_'))  # 7
    # print(match_str8('Abb2adf_av8U9324abbKbfsgfd_'))  # 8
    # print(match_str9('abb2badf_av89324abbbfsgfabd6464a5466b_'))  # 9
    print(match_str10('Word f_av89324abbbfsgfabd6464a5466b_'))  # 10
