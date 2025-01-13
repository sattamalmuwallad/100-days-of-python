def format_name(f_name, l_name):
    
    if f_name == "" and l_name == "":
        return "You did not provide valid inputs"
    new_f_name = f_name.title()
    new_l_name = l_name.title()
    return f"{new_f_name} {new_l_name}"


print(format_name("AnGEla", "YU"))
