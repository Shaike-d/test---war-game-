



def Value_Extraction(str_card):
    value = ""
    for char in str_card:
        if char.isdigit():
            value += char
    return int(value)