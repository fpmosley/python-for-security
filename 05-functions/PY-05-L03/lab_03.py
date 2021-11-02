global_var = 5
changed_global_var = 20


def local_change():
    global_var = 10
    print(f"Inside function. 'global_var' value: {global_var}")
    global changed_global_var
    changed_global_var += 5
    print(f"Inside function. 'changed_global_var' value: {changed_global_var}")


local_change()
print(f"Outside function. 'global_var' value: {global_var}")
print(f"Outside function. 'changed_global_var' value: {changed_global_var}")
