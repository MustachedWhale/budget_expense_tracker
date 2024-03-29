# Adds some global utility functions.

def name_capitalise(name):
    name_list = name.split()
    new_name = ''
    for name in name_list:
        if name[0].islower():
            new_name = new_name + name.capitalize() + ' '
        else:
            new_name = new_name + name + ' '
    new_name = new_name[:-1]
    return new_name

new_name = name_capitalise('..hello errrm 127360182bsdfja;s')
print(new_name)