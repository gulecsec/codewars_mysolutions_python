def password(string):
    if len(string) >= 8 and any(char.islower() for char in string) and any(char.isupper() for char in string) == True and any(char.isalnum() for char in string) and any(char.isdigit() for char in string) and any(char.isalpha() for char in string):
        return True
    return False