user = {
    "name": "Anonymous",
    "age": 23,
    "is_learning": True
}

for key, value in user.items():
	print(key,":",value)
	
print(user.get("email","Not provided"))