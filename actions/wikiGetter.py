import wikipedia


#print (wikipedia.search("intelligence artificiel"))
#print (wikipedia.page("programming").url)
def getFromwikipedia():  
    try:
        res = wikipedia.summary("hello world" ,sentences=2) 
    except wikipedia.exceptions.DisambiguationError as e:
        res = e 
    
    return res
