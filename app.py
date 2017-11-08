import twitter
import os
import json
# connecting to twitter api
with open('data.json' ) as config_file:
    config_data = json.load(config_file)

cKEY = config_data['consumer_key']
cSecret = config_data['consumer_secret']
aToken = config_data['access_token']
aSecret = config_data['access_secret']

# authenticate your twitter app credentials already saved in the 'pickle'

# auth = twitter.oauth.OAuth(Twitter['Access Token'],
#                            Twitter['Access Token Secret'],
#                            Twitter['Consumer Key'],
#                            Twitter['Consumer Secret'])
auth = twitter.oauth.OAuth(aToken,
                           aSecret,
                           cKEY,
                           cSecret,)

twitter_api = twitter.Twitter(auth=auth)

# Nothing to see by displaying twitter_api except that it's now a
# defined variable

print(twitter_api)

WORLD_WOE_ID = 1
NIG_WOE_ID = 23424908
LOCAL_WOE_ID= 1398823


# Prefix ID with the underscore for query string parameterization.
# Without the underscore, the twitter package appends the ID value
# to the URL itself as a special case keyword argument.

world_trends = twitter_api.trends.place(_id= WORLD_WOE_ID)
Nig_trends = twitter_api.trends.place(_id=NIG_WOE_ID)
local_trends = twitter_api.trends.place(_id=LOCAL_WOE_ID)

trends=local_trends
date = trends[0]['as_of']
location = trends[0]['locations']
state = location[0]['name']
woeid = location[0]['woeid']

y = trends[0]['trends']

# creating a list of tuple contain data from twitter trends
listTuple = []
for dic in y:
    tup=tuple(list(dic.values()))
    listTuple.append(tup)

# len(listTuple)
# listTuple[0]
    


import sqlite3 as lite
from sqlite3 import Error
 
# a function that creates database(db)
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = lite.connect(db_file)
        print(lite.version)
        print('Database successfully created!!')
    except Error as e:
        print(e)
    finally:
        conn.close()

# create the db using the function
if __name__ == '__main__':
    create_connection("tweetdb.db")

# connect to the db
conn = lite.connect('tweetdb.db')

# initialize the cursor
c = conn.cursor()
if conn:
    print('Opened db successfuly!')



# # create table within the db
# conn.execute('''CREATE TABLE Tweets
#              ( 
#               NAME CHAR(200)          NOT NULL,
#               URL  CHAR(200)          NOT NULL,
#               PROMOTED_CONTENT CHAR(200) ,
#               QUERY CHAR(200),
#               TWEET_VOLUME CHAR(200));''')


# #insert values into table
# c.executemany("INSERT INTO Tweets VALUES(?,?,?,?,?)", listTuple)

# # commit values into db
# conn.commit()
# print(len(listTuple),' Records successfully entered into db!')

# #close connection to db
# conn.close()


from bottle import route, run, template



@route('/trends')
def show_tweet():
    conn = lite.connect('tweetdb.db')
    c = conn.cursor()
    c.execute("SELECT NAME, URL FROM Tweets")
    data = c.fetchall()
    print('i am ready')
    c.close()
    output = template('twitter_temp', twitter_trends=data, s=state, date = date, woeid = woeid)
    return output

run(host='0.0.0.0', port=8080)