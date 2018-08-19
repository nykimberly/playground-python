#Modify name to abbreviated version

def abbrevName(name):
    # convert to list to easily iterate over words
    name_arr = name.split()
    # iterate through list; track index
    for i, e in enumerate(name_arr):
        # check for middle name condition (not first or last)
        if (i != 0) & (i != (len(name_arr)-1)):
            # keep only the first letter
            name_arr[i] = e[0] + "."
    return " ".join(name_arr)


abbrevName("Kimberly Van Anh Nguyen")
