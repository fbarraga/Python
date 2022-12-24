def group_list(group, users):
    user=""
    cadena=""
    for user in users:
        cadena = cadena + user + ", "
    cadena = cadena[0:len(cadena)-2]
    members = "{}: {}".format(group, cadena)
    return members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"