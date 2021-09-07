
#-------------------JSON----------------------------------
def MyJson():
  import json
  #Convert from JSON to Python:
  x='{"Name":"Helal" ,"age":26}'
  y=json.loads(x)
  print(y["Name"])

  #Convert from Python to JSON:
  x={
    "name": "John",
    "age": 30,
    "city": "New York"
  }

  y=json.dumps(x)
  print(y)

  #Convert Python objects into JSON strings, and print the values:
  print(json.dumps({"name": "John", "age": 30}))
  print(json.dumps(["apple", "bananas"]))
  print(json.dumps(("apple", "bananas")))
  print(json.dumps("hello"))
  print(json.dumps(42))
  print(json.dumps(31.76))
  print(json.dumps(True))
  print(json.dumps(False))
  print(json.dumps(None))

