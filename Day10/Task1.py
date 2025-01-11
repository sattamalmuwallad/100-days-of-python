def format_name(f_name, l_name):
    new_f_name= f_name.title()
    new_l_name= l_name.title()
    return f"{new_f_name} {new_l_name}"
print(format_name("satam","LALD"))

def function_1(text):
    return text + text


def function_2(text):
    return text.title()


output = function_2(function_1("hello"))
print(output)