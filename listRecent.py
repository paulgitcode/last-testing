import lastCall

# Variables to define

user = 'paulymusic'
limit = 60
method1 = 'method'
method2 = 'user.getRecentTracks'

# Track class

class track:
  def __init__(self, nameA, nameT,nameAl,date):
    self.nameArtist = nameA
    self.nameTrack = nameT
    self.nameAlbum = nameAl
    self.dateTrack = date

# Function to create list of Recent Track class objects

def createRecentTracksList(inJ,inLimit):

    aTrackList = []

    i = 0
    l = inLimit
    while i < l:

        getNameArtist = inJ.json()['recenttracks']['track'][i]['artist']['#text']
        getNameTrack = inJ.json()['recenttracks']['track'][i]['name']
        getNameAlbum = inJ.json()['recenttracks']['track'][i]['album']['#text']
        getDateTrack = inJ.json()['recenttracks']['track'][i]['date']['#text']

        a = track(getNameArtist,getNameTrack,getNameAlbum,getDateTrack)

        aTrackList.append(a)
        i += 1

    return aTrackList

# Function to print out all results in the Recent Track list.

def printRecentTrackList(inList):

    lenList = len(inList)
    i = 0
    textName = '|Recent Track List|'
    textDiv = ':'
    textIndent = '       '
    textFrom = 'from the album'
    textOn = 'on'

    print('-----------------------')
    print(textName,textDiv)
    print('-----------------------')

    while i < lenList:

        
        print(inList[i].nameArtist,"\n",textIndent,'"',inList[i].nameTrack,'"',textFrom,'"',inList[i].nameAlbum,'"',textOn,inList[i].dateTrack)

        i += 1

    return

# Calling the results

r = lastCall.setValuesCall(method1,method2,user,limit)

# Creating the recent track list

a1 = createRecentTracksList(r,limit)

# Printing the track list

printRecentTrackList(a1)
