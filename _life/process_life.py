from collections import defaultdict
import json
import sys

def getDate(event, event_keys):
    if 'from' in event_keys:
        if 'to' in event_keys:
            return "{0}-{1}".format(event['from'], event['to'])
        else:
            return "{0}-~".format(event['from'])
    elif 'on' in event_keys:
        return "{0}".format(event['on'])

def getDescription(event, event_keys):
    if 'website' in event_keys:
        return "[{0}]({1})".format(event['description'], event['website'])
    else:
        return "{0}".format(event['description'])

def getProfessionalDescription(event, event_keys):
    return "[{0} at {1}, {2}]({3})".format(event['title'], event['company'], event['location'], event['website'])

def main():
    if len(sys.argv) != 3:
        print ("usage: python process_life.py username path_to_life.json > life.md")
        return
    else:
        username = sys.argv[1]
        file = open(sys.argv[2])

    print "@{0}'s life".format(username)

    for line in file:
        event = json.loads(line)
        event_keys = [e.encode('utf-8') for e in event]

        date = getDate(event, event_keys)
        if event['category'] == 'Professional':
            entry = "{0} {1}".format(date, getProfessionalDescription(event, event_keys))
        else:
            entry = "{0} {1}".format(date, getDescription(event, event_keys))

        print "- {0}".format(entry)

    file.close()


if __name__ == '__main__':
    main()
