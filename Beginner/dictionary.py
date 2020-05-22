post = {
    "user_id": 209,
    "message": "D5 E5 C4",
    "language": "English",
    "datetime": "203123142131213",
    "location": (44.590, -104.741),
}
print(type(post))
post2 = dict(message="ss cotopaxi", language="english")
print(post2)
post2["user_id"] = 209
post2["datatime"] = "12312412313"
print(post2)
print(post["message"])
if "location" in post2:
    print(post2["location"])
else:
    print("no data")

for key in post.keys():
    value = post[key]
    print(key, "=", value)
for key, value in post.items():
    print(key, "=", value)
