import json

info = '{"name":"Dagaga", "age":18, "skills":["math","physics","programming","philosophy"], "status":"single"}'
data = json.loads(info)
with open("file.txt", "w") as file:
    json.dump(data, file, indent=3)

print("JSON parsed and saved successfully.")
