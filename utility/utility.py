import json
import json
import boto3
import time
import logging

import inspect

client = boto3.client('logs', region_name="eu-west-1")
loggroup = 'newtest'
logstream = 'teststream1'


def writetofile(filepath, templist, data):
    try:
        with open(filepath, 'w') as f:
            templist.append(data)
            json.dump(templist, f, indent=4, separators=(',', ': '))
    except IOError:
        print('Save to file failed'+IOError.message)


def deletefromfile(filepath, templist, id):
    try:
        with open(filepath, 'w') as f:
            [templist.pop(templist.index(x))
             for x in templist if x["productid"] == id]
            json.dump(templist, f, indent=4, separators=(',', ': '))
    except IOError:
        print('Save to file failed'+IOError.message)


def readfromfile(filepath, templist):
    try:
        with open(filepath) as f:
            templist = json.load(f)
            return templist
    except IOError:
        print('Read from file failed'+IOError.message)


def logtoFile(loglevel, temp):
    logformat = 'loglevel: %(levelname)s timestamp : %(asctime)s , "output": %(message)s'
    logging.basicConfig(filename='debug.log',
                        level=logging.DEBUG, format=logformat)
    if loglevel == 'INFO':
        logging.info(json.dumps(temp))
    if loglevel == 'WARNING':
        logging.warning(json.dumps(temp))
    if loglevel == 'ERROR':
        logging.error(json.dumps(temp))
        
    print("Logs for %s() function added to file successfully" %
          inspect.stack()[1].function)

def sequenceToken():
    logdescribe = client.describe_log_streams(
    logGroupName=loggroup, logStreamNamePrefix=logstream)
    sequenceToken =  logdescribe['logStreams'][0]['uploadSequenceToken']
    return sequenceToken


def sendlogstocloudwatch(loglevel, temp, details):
    token = sequenceToken()
    logmessage = {
        "loglevel ": loglevel,
        "functioncalled": "%s()" % inspect.stack()[1].function ,
        "details": details,
        "output": temp
    }
    log_event = {
        'logGroupName': loggroup,
        'logStreamName': logstream,
        'logEvents': [
                {
                    'timestamp': int(round(time.time() * 1000)),
                    'message': json.dumps(logmessage),
                },
        ],
        'sequenceToken':  token
    }
    client.put_log_events(**log_event)
    print("Logs for %s() function call sent successfully" %
          inspect.stack()[1].function)
