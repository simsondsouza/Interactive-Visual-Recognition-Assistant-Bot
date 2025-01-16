import wikipedia

def search(statement):
    query = statement.replace("search","")
    query = statement.replace("find","")
    query = statement.replace("google search","")

    result = wikipedia.summary(query,3)
    return result
 
    