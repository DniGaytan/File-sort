import os
import json

def encodePath(path):
    encodedPath = ''
    for c in path:
        if ord(c) is 92:
            encodedPath = encodedPath + ''.join('\\')
        else:
            encodedPath = encodedPath + ''.join(c)
    return encodedPath

json_data = {}
with open('keywords.json') as json_file:
    json_str = json_file.read()
    json_data = json.loads(json_str)

print(json_data['\\carpeta-prueba'])


#Reads the destination path from data.txt
destPath = ''
with open('data.txt', 'r') as f:
    destPath = encodePath(f.read())





#os.path.isfile("bob.txt")
#os.listdir(path)
