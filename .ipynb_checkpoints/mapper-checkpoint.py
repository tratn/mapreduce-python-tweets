topic = 'vaccines'   # replace topic here 

def mapper_count_topic(news_chunk, keyword=topic): 
    """Given a news chunk and a topic, return the occurence of the topic and the tweet ID as dictionary"""
    occurence = {'keyword': topic, 'count': 0, 'ids' : []}
    # convert to lowercase 
    news_chunk = [x.lower() for x in news_chunk]
    # count the occurence and also keep track of index of the line 
    for tweet in news_chunk: 
        if topic in tweet:
            occurence['count'] += 1
            occurence['ids'].append(tweet.split("|")[0])
    return occurence
            

