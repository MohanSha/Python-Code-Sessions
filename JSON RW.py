import json
 
data = {
    "FirstName":"Mohan",
    "MiddleName":"S",
    "LastName":"Sha",
    "DateOfBirth":"26-05-1996",
    "Contact":{
        "Phone":9551175171,
        "Email":"mohansha@qubecinema.com"
    },
    "Address":[
        {
            "Type":"Office",
            "ZipNumber":600004,
            "Street":"Dr Ranga Road",
            "City":"Chennai",
            "Country":"India"
        },
        {
            "Type":"Home",
            "ZipNumber":600002,
            "Street":"Mangapathy St",
            "City":"Chennai",
            "Country":"India"
        }
    ]
}
 
#json.dumps() method turns a Python data structure into JSON:
jsonData = json.dumps(data)
print(jsonData)
 
# Writing JSON data into a file called JSONData.json
#Encode JSON data
with open('JSONData.json', 'w') as f:
     json.dump(jsonData, f)

 
input = '''
{
    "FirstName":"Mohan",
    "MiddleName":"S",
    "LastName":"Sha",
    "DateOfBirth":"26-05-1996",
    "Contact":{
        "Phone":9551175171,
        "Email":"mohan.sha@qubecinema.com"
    },
    "Address":[
        {
            "Type":"Office",
            "ZipNumber":600004,
            "Street":"Dr Ranga Road",
            "City":"Chennai",
            "Country":"India"
        },
        {
            "Type":"Home",
            "ZipNumber":600002,
            "Street":"Mangapathy St",
            "City":"Chennai",
            "Country":"India"
        }
    ]
}
        '''
print(type(input))
jsonObjectInfo = json.loads(input)
print(type(jsonObjectInfo))
print(jsonObjectInfo)
print("First Name is {0}".format(jsonObjectInfo['FirstName']))
print("Middle Name is {0}".format(jsonObjectInfo['MiddleName']))
print("Last Name is {0}".format(jsonObjectInfo['LastName']))
print("Date of Birth is {0}".format(jsonObjectInfo['DateOfBirth']))
print("Phone Number is {0}".format(jsonObjectInfo['Contact']['Phone']))
print("Email ID is is {0}".format(jsonObjectInfo['Contact']['Email']))
print("-----------------**************---------------")
for eachJsonObject in jsonObjectInfo['Address']:
    print("Address Type is {0}".format(eachJsonObject['Type']))
    print("Zip Number is {0}".format(eachJsonObject['ZipNumber']))
    print("Street Name is {0}".format(eachJsonObject['Street']))
    print("City Name is {0}".format(eachJsonObject['City']))
    print("Country Name is {0}".format(eachJsonObject['Country']))
    print("-----------------**************---------------")
 
 
# Reading JSON data back from a file called JSONData.json
#Decode JSON Data
with open('JSONData.json', 'r') as f:
     data = json.load(f)
 
print(data)


