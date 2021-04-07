import wikipedia


#wikipedia.summary(wikipedia.search(title , results=1),sentences=2)
#wikipedia.page(wikipedia.search(title , results=1)).content
def getFromwikipedia(title):  
    try:
        res = wikipedia.summary(wikipedia.search(wikipedia.page(title).title , results=1),sentences=2)
    except wikipedia.exceptions.DisambiguationError as e:
        res = e 
    
    return res
