users=[{"name": "ali", "role": "admin"} , {"name": "reza" , "role": "user"} , { "name": "sara" , "role": "admin"} ,]
unique_roles=set(user["role"] for user in users)
print("unique roles:",unique_roles)
