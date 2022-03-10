# main.py
import json

from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
        return jsonStr #This is the json string which returns all the users above age 10

pepole_string = '''
{
  "people": [
    {
      "name": "Tom",
      "age": 11
    },
    {
      "name": "Arik",
      "age": 35
    },
    {
      "name": "Adam",
      "age": 7
    }
  ]
}
'''

data = json.loads(pepole_string)
my_output = []
#Filtering user above age 10
for person in data['people']:
        if person['age'] > 10:
            my_output.append([person['name'] + ":" + str(person['age'])])# Concatenate string + int from json string


print(my_output)#for internal testing
aList = [my_output]
jsonStr = json.dumps(aList)#from array to json
print(jsonStr)#for internal testing






if __name__ == "__main__":
        app.run(host="127.0.0.1", port=8000, debug=True)
