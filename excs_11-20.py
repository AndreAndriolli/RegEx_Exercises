import re
# Exercices from https://www.w3resource.com/python-exercises/re/


# 11. Write a Python program that matches a word at the end of a string, with optional punctuation
def match_str(_str):
    pattern = re.compile(r' [A-Za-z]+[.!?]*$')
    # pattern = re.compile(r' [A-Za-z]+[\W]{0,3}$')  # It ll consider a lot of carct. that may not be useful.
    match = re.search(pattern, _str)
    if match:
        # print(match)
        # print(match.group())
        pass
    return True if match else False


# 12. Write a Python program that matches a word containing 'z'.
def match_str2(_str):
    pattern = re.compile(r'\b[A-Za-z]*?[Zz][A-Za-z]*?\b')
    match = re.findall(pattern, _str)
    if match:
        # print(match)
        # print(match.group())
        pass
    return match if not None else False


# 13. Write a Python program that matches a word containing 'z', not the start or end of the word.
def match_str3(_str):
    # 'z' word not in the start or in the end of str
    # pattern = re.compile(r'[^^]\b[A-Za-z]*?[Zz][A-Za-z]*?\b[^$]')
    # 'z' word not in the start or in the end of word
    pattern = re.compile(r'\b[A-Ya-y][A-Za-z][Zz]+[A-Za-z]*?[A-Ya-y]*?\b')
    match = re.findall(pattern, _str)
    if match:
        # print(match)
        # print(match.group())
        pass
    return match if not None else False


#  14. Write a Python program to match a string that contains only upper and lowercase letters,
#  numbers, and underscores.
def match_str4(_str):
    pattern = re.compile(r'\b\w+?\b')
    match = re.findall(pattern, _str)
    return match if match else False


# 15. Write a Python program that starts each string with a specific number.
def match_str5(_str, num):
    pattern = re.compile(fr'\b{num}-\w*\b')
    match = re.findall(pattern, _str)
    return match if match else False


# 16. Write a Python program to remove leading zeros from an IP address.
def match_str6(ip_address):
    # pattern = re.compile(r'[1-9][0-9]?[0-9]?\.?')
    match = re.sub(r'\.[0]*', '.', ip_address)
    match2 = re.sub(r'^[0]*', '', match)
    match3 = re.sub(r'\.\.', '.0.', match2)
    return match3


# 17. Write a Python program to check for a number at the end of a string.
def match_str7(_str, num_find):
    pattern = re.compile(fr'\b[A-Za-z0-9]*?{num_find}\b')
    match = re.findall(pattern, _str)
    return match


# Write a Python program to search for numbers (0-9) of length between 1 and 3 in a given string.
# "Exercises number 1, 12, 13, and 345 are important"
def match_str8(_str):
    pattern = re.compile(r'\b[0-9]{1,3}\b')
    match = re.findall(pattern, _str)
    return match


# 19. Write a Python program to search for literal strings within a string.
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox', 'dog', 'horse'
def match_str9(_str, word):
    pattern = re.compile(fr'\b{word}\b')
    match = re.findall(pattern, _str)
    return match if match else False


# 20. Write a Python program to search for a literal string in a string
# and also find the location within the original string where the pattern occurs.
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox'
def match_str10(_str, word):
    pattern = re.compile(fr'\b{word}\b')
    match = re.search(pattern, _str)
    return match


if __name__ == "__main__":
    # print(match_str('Potato f_av89324abbbfsgfabd6464a Word...'))  # 1
    # print(match_str2('mouse Zebra sorry potato Fuzzy shoes quiz keyboard'))  # 2
    # print(match_str3('Zoom m_ouse Zebra sorry potato Fuzzy shoes quiz keyboard Zonai izzyzdsf'))  # 3
    # print(match_str4('Zoom mouse Zebra sorry potato Fuzzy shoes q2uiz keyboard Zonai izzyzdsf'))  # 4
    # print(match_str5('5-Zoom 2-mouse 1-Zebra 4-sorry 5-potato 2-Fuzzy ', 2))  # 5
    # print(match_str6('002.068.000.001'))  # 6
    # print(match_str7('Zoom1 mouse1 Zebra2 sorry3 potato5 Fuzzy8 shoes13 quiz21 keyboard34 ', 1))  # 7
    # print(match_str8('1 12 13 345 5555 485 2 3 5'))  # 8
    # print(match_str9('The quick brown fox jumps over the lazy dog.', 'fox'))  # 9
    print(match_str10('The quick brown fox jumps over the lazy fox. fox', 'fox'))  # 10
