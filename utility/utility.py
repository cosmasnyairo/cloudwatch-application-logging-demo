import json


def writetofile(self, filepath, templist, data):
        try:
            with open(filepath, 'w') as f:
                templist.append(data)
                json.dump(templist, f, indent=4, separators=(',', ': '))
        except IOError:
            print('Save to file failed'+IOError.message)

def deletefromfile(self, filepath, templist, id):
        try:
            with open(filepath, 'w') as f:
                [templist.pop(templist.index(x))
                 for x in templist if x["productid"] == id]
                json.dump(templist, f, indent=4, separators=(',', ': '))
        except IOError:
            print('Save to file failed'+IOError.message)

def readfromfile(self, filepath, templist):
        try:
            with open(filepath) as f:
                templist = json.load(f)
                return templist
        except IOError:
            print('Read from file failed'+IOError.message)
