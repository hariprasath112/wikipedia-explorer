import wikipedia
import random
def searchselector():
    global searchselect
    searchselect=int(input('Select an option from the list (0 to '+ str(len(resultlist)-1)+'): '))
def randomsearchselector():
    global searchselect
    searchselect=random.randrange(len(resultlist))

def getpage(searchselect):
    global page
    page=wikipedia.page(resultlist[searchselect], auto_suggest=False)
    
def getrandompage(topic):
    global page
    page=wikipedia.page(topic)

def getsummary(page):
    str="_"
    print(str*64)
    print(page.title)
    print(str*64)
    print(page.summary)
    print(str*64)

def getcontent(page):
    str="_"
    print(str*64)
    print(page.content)
    print(str*64)

def exitfunc():
    n=input('Do you want to exit? y/n: ')
    if (n=="y"):
        exit()
    else:
        searchfunc()

def newsearchfunc():
    secondchoice=input("Do you want to make new search? y/n: ")
    if (secondchoice=="y"):
        searchfunc()
    else:
        linkaskfunc()
def linkaskfunc():
    secondchoice=input("Do you want to jump to random link within current page? y/n: ")
    if (secondchoice=="y"):
        linkfunc()
    else:
        exitfunc()
def linkfunc():
    global searchselect
    global page
    global resultlist
    resultlist=page.links
    searchselect=random.randrange(len(resultlist))
    getpage(searchselect)
    decidedisplaytype=input("Do you want to see a summary, no means full page? y/n: ")
    if (decidedisplaytype=="y"):
        getsummary(page)
    else:
        getcontent(page)
    linkaskfunc()
def searchfunc():
    global inputsearch
    global resultlist
    askrandom=input("Generate random article? y/n: ")
    if (askrandom=="y"):
        topic=wikipedia.random(1)
        getrandompage(topic)
    else:
        inputsearch=input('Enter a search term to search in Wikipedia: ')
        resultlist=list(wikipedia.search(inputsearch))
        for i in range(len(resultlist)):
                print(i,"- ",resultlist[i], end='\n')
        decideselecttype=input("Do you want to select search list randomly? y/n: ")
        if (decideselecttype=="y"):
            randomsearchselector()
        else:
            searchselector()
        getpage(searchselect)
    decidedisplaytype=input("Do you want to see a summary, no means full page? y/n: ")
    if (decidedisplaytype=="y"):
        getsummary(page)
    else:
        getcontent(page)
    newsearchfunc()
searchfunc()
