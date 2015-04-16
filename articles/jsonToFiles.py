import json
def jsonToFiles(journal="oxford"):
    data = open("./" + journal + "/" + journal + ".json")
    articles = json.load(data)
    for article in articles:
        _file = open("./" + journal + "/files/" + article["title"].encode('utf-8'), "w+")
        _file.write(article["abstract"].encode('utf-8'))
        _file.close()
