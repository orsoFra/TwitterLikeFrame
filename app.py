from flask import Flask,redirect, render_template, request, session, abort
import tweepy
from tweepy.api import API
from dotenv import load_dotenv
import datetime
import re
import os
from datetime import timedelta
from TweetInfo import getTweetId

'''
AUTHENTICATION
'''
#use of env variables - need to be set in a external file or in the system
load_dotenv('info/.env')
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
bearer_token = os.getenv('BEARER_TOKEN')
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth.secure = True
api = tweepy.API(auth)

'''
METHODS
'''

def printImg(name,image,date,id):
    string= '<div class="row"><div class="col-sm-3"></div><div class="col-sm-6"><div class="text-center"><p>'+ name+"  -  "+date +" - <a href='https://twitter.com/twitter/statuses/"+ str(id) +"'>See on Twitter</a>"+'</p><img class="img-fluid mx-auto d-block" src='+ image +'></div></div><div class="col-sm-3"></div></div><hr>'
    return string

def printCarousel(name,images,date,nCar,id):
    carousel='<div id="carouselno'+str(nCar)+'" class="carousel slide" data-bs-interval="false" ><div class="carousel-inner" data-bs-interval="false"><div class="carousel-item active" data-interval="false"> <img src="'+ images[0] +'" class="d-block w-100" alt="..."></div>'
    for i in range(1,len(images),1):
        carousel+='<div class="carousel-item"> <img src="'+ images[i] +'" class="d-block w-100" alt="..."></div>'
    carousel+='</div><button class="carousel-control-prev" type="button" data-bs-target="#carouselno'+str(nCar)+'" data-bs-slide="prev"><span class="carousel-control-prev-icon" aria-hidden="true"></span><span class="visually-hidden">Previous</span></button><button class="carousel-control-next" type="button" data-bs-target="#carouselno'+str(nCar)+'" data-bs-slide="next"><span class="carousel-control-next-icon" aria-hidden="true"></span><span class="visually-hidden">Next</span></button></div>'
    string = '<div class="row"><div class="col-sm-3"></div><div class="col-sm-6"><div class="text-center"><p>'+ name+"  -  "+date +" - <a href='https://twitter.com/twitter/statuses/"+ str(id) +"'>See on Twitter</a>"+'</p></div>'+carousel+'</div><div class="col-sm-3"></div></div><hr>'
    return string


'''
FLASK APP
'''
DEBUG=True
app = Flask(__name__)

@app.route("/")
def form():
    return render_template('form.html')

@app.route("/home",methods=['POST','GET'])
def home():
    if(request.method == 'POST' or request.method == 'GET'):
        #get data from the form 
        username = request.form['User']
        startDate=request.form['startDate']
        endDate=request.form['endDate']
        #get a dummy date which is the date prior to the start date
        match = re.search('\d{4}-\d{2}-\d{2}', startDate)
        dateDummy = datetime.datetime.strptime(match.group(), '%Y-%m-%d').date()
        dateDummy = dateDummy + timedelta(days=-1)
        #get a dummy date which is the date prior to the end date
        match2 = re.search('\d{4}-\d{2}-\d{2}', endDate)
        dateDummy2 = datetime.datetime.strptime(match2.group(), '%Y-%m-%d').date()
        dateDummy2 = dateDummy2 + timedelta(days=-1)
        #print(username)
        '''print(startDate) #things for testing
        print(endDate)
        print(dateDummy)
        print(dateDummy2)'''
        #empty data list for storing the html content
        data = [] 
        #counter of the multi image tweets   
        countCar=0
        #if there's a text tweet
        isTweet=True
        #apply a filtering date after getting all the data needed ----- USING getTweetId with different dates because advanced search sucks
        try:
            for favorite in tweepy.Cursor(api.get_favorites, screen_name=username,include_entities=True,since_id=getTweetId(str(dateDummy),startDate),max_id=getTweetId(str(dateDummy2),endDate)).items(150):
                
                if('media' in favorite.entities): #NB: the liked tweets get sorted by POSTING DATE NOT LIKING DATE  
                    leng = len(favorite.extended_entities['media'])
                    if(leng>1):#if it is a multi image tweet
                        images=[]#list for storing the multiple images
                        countCar+=1
                        for i in range(0,leng,1):
                            images.append(favorite.extended_entities['media'][i]['media_url'])#append the images to the list
                        #print the carousel
                        data.append(printCarousel(str(favorite.user.name),images,str(favorite.created_at.date()),countCar,favorite.id))
                    else:
                        #print the single image
                        data.append(printImg(str(favorite.user.name),str(favorite.entities['media'][0]['media_url']),str(favorite.created_at.date()),favorite.id))
                isTweet=False
        except:
            isTweet=False
            data.append('<div class="row"><div class="col-sm-3"></div><div class="col-sm-6"><div class="text-center"><p>It appears that the username you requested does not exist, try another!</p></div></div><div class="col-sm-3"></div></div>')
        if(len(data) == 0 and isTweet):
            #printed in case of(see content)
            data.append('<div class="row"><div class="col-sm-3"></div><div class="col-sm-6"><div class="text-center"><p>Some tweets exist, but they do not contain any images!</p></div></div><div class="col-sm-3"></div></div>')
    return render_template('index.html',data=data)
if __name__ == "__main__":
    app.run()