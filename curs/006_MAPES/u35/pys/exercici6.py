def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for groups, users in group_dictionary.items():
        # Now go through the users in the group
        for user in users:
            if user in user_groups:
                user_groups[user].append(groups)
            else:
                user_groups[user] = [groups]
    return user_groups

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))