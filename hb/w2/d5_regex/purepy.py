def is_phone_dashes_intl_ac(s):
    """Match phone, allowing dashes, leading 1, and (area code). """

    if s.startswith("1-"):
        s = s[2:]
    elif s.startswith("1 "):
        s = s[2:]
    elif s.startswith("1"):
        s = s[1:]
    if len(s) == 10 and s.isdigit():
        return True
    if (s[0] == "(" and s[4:6] == ") " and len(s) == 14 and
        s[1:3].isdigit() and s[6:9].isdigit() and s[10:].isdigit()):
        return True
    if (s[3] == "-" and s[7] == "-" and len(s) == 12 and
        s[0:2].isdigit() and s[4:7].isdigit() and s[8:].isdigit()):
        return True
    return False

if __name__ == "__main__":
    input_string = input("Phone number checker: ")
    print(is_phone_dashes_intl_ac(input_string))
