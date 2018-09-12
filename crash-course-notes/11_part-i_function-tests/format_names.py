def format_name_title(first, last, middle=''):
    if middle == '':
        full_name = first + ' ' + last
    else:
        full_name = first + ' ' + middle + ' ' + last
    return full_name.title()
