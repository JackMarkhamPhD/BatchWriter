import os
if os.path.exists("output.txt"):
  os.remove("output.txt")


with open('BodyText.txt') as f:
    body = f.readlines()
body = "".join(body)



# varDict = {}
import csv

varNameList = []

with open('output.txt','a') as outFile:
    with open('Variables.csv') as varFile:
        reader = csv.reader(varFile)

        for i, row in enumerate(reader):
            if i == 0:
                for varName in row:
                    varNameList.append(varName)
            else:
                newBody = body
                for n, var in enumerate(row):
                    newBody= newBody.replace(varNameList[n], row[n])
                print(newBody)
                outFile.write(newBody+"\n----------------\n")
