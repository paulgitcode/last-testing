#################

import lastCall

##### Variables to define #####

user = 'paulymusic'
limit = 200

method1 = 'method'
method2 = 'library.getArtists'

# Artist class and related functions

class artist:
  def __init__(self, name, playcount):
    self.name = name
    self.playcount = playcount

# Function to create list of Artist class objects

def createArtistList(inJ,inLimit):

    aList = []

    i = 0
    l = inLimit
    while i < l:

        getName = inJ.json()['artists']['artist'][i]['name']
        getCount = inJ.json()['artists']['artist'][i]['playcount']

        a = artist(getName,getCount)

        aList.append(a)
        i += 1

    return aList

# Function to print out all results in the Artist List.

def printArtistList(inList):

    lenList = len(inList)
    i = 0
    textName = '|Artist|'
    textCount = '|Playcount|'
    textDiv = ':'

    print('-----------------------')
    print(textName,textDiv,textCount)
    print('-----------------------')

    while i < lenList:

        
        print(inList[i].name,textDiv,inList[i].playcount)

        i += 1

    return

# Calling the results

r = lastCall.setValuesCall(method1,method2,user,limit)

# Creating the artist list

a1 = createArtistList(r,limit)

# Printing the artist list

printArtistList(a1)
