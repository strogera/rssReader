import feedparser

rssFeeds=open('rssFeeds.txt', 'r').readlines()

responces={}
for feed in rssFeeds:
    responces[feed] = feedparser.parse(feed)

for feed in responces:
    print(feed + ' : ' )
    for entry in responces[feed].entries:
        print('\t' + entry.title + ' - ' + entry.link)

    print()
