# https://cloud.google.com/translate/docs/languages
# This project is made by Paramdeep Singh Gill
import time

import os
import smtplib
import requests, sys, webbrowser, bs4
from googletrans import Translator
import subprocess as sp
import tweepy
import confg
import pyttsx3
engine = pyttsx3.init()



for x in range(3):
  print('-', flush=True, end="")
  time.sleep(0.5)
print("\n")



def password(q1):
  for x in range(5):
    time.sleep(1)
    print("-", flush=True, end='')
  f=open("password.txt", "r")
  v = f.read()
  print("\n" + v)
  var = input("-").lower()
  clean(var)

def learn(q1):
  x = input("Question.")
  f=open("q1.txt","w")
  f.write(x)
  f.close()
  y = input("Answer.")
  f=open("a1.txt","w")
  f.write(y)
  f.close()
  f=open("q1.txt", "r")
  q1 = f.read()
  var = input("-").lower()
  clean(var, q1)
  

def qa1(q1):
  f=open("a1.txt", "r")
  var = f.read()
  print(var)
  engine.say(var)
  engine.runAndWait()
  var = input("-").lower()
  clean(var, q1)

def remember(q1):  
  engine.say("What do you want me to remember ?")
  engine.runAndWait()
  h = input("What do you want me to remember ?").lower()
  b = ".!?@#$"
  for char in b:
      h = h.replace(char,"")  
  if h == "history":
    print("This is what you told me to remember last time.")
    engine.say("This is what you told me to remember last time.")
    engine.runAndWait()
    f=open("remember.txt", "r")
    var = f.read()
    print(var)
    var = input("-").lower()
    clean(var, q1)
  else:
    f=open("remember.txt", "a")
    f.write("\n" + h)
    f.close()
    print("Ok, Sir.")
    engine.say("Ok, Sir.")
    engine.runAndWait()
    var = input("-").lower()
    clean(var, q1)


def search(q1):
  engine.say("What do you want to search sir?")
  engine.runAndWait()
  var = input("What do you want to search sir?:")
  res = requests.get('http://google.com/search?q=' + var )
  res.raise_for_status()
  soup = bs4.BeautifulSoup(res.text, "html.parser")
  linkElements = soup.select('.r a')
  print("1-->  " + str(linkElements[1]) + "\n")
  print("2-->  " + str(linkElements[2]) + "\n")
  print("3-->  " + str(linkElements[3]) + "\n")
  print("4-->  " + str(linkElements[4]) + "\n")
  engine.say("Do you want to open this in a browser/")
  engine.runAndWait()
  v = input("Do you want to open this in a browser?(y/n)")
  if v == "y":
    print("As your wish sir.")
    engine.say("As your wish sir.")
    engine.runAndWait()
    time.sleep(1)
    webbrowser.open('http://google.com/search?q=' + var)
    var = input("-").lower()
    clean(var, q1)
  else:
    var = input("-").lower()
    clean(var, q1)

def translate(q1):
  engine.say("What do you want to translate sir?")
  engine.runAndWait()
  v = input("What do you want to translate sir?:")  
  engine.say("In which language do you want to it translate sir?:")
  engine.runAndWait()
  w = input("In which language do you want to it translate sir?:")
  translator = Translator()
  k = translator.translate(v, dest=w)
  print(k)
  var = input("-").lower()
  clean(var, q1)

def email(q1):
  engine.say("What is the message sir?")
  engine.runAndWait()
  w = input("What is the message sir?")
  engine.say("Whom you want to send this message?")
  engine.runAndWait()
  n = input("Whom you want to send this message?")
  myemail = confg.my_email
  if n == 'me':
    receiver_email = myemail
  else:
    receiver_email = str(n)
  
  s = confg.gmail_server
  server = smtplib.SMTP(s,587)
  server.starttls()
  server.login(myemail, confg.email_password)
  message = str(w)
  server.sendmail(myemail, receiver_email, message)
  server.quit()
  var = input("-").lower()
  clean(var, q1)

def tweet(q1):
  engine.say("What is the tweet sir?")
  engine.runAndWait()
  w = input("What is the tweet sir?")
  consumer_key = confg.consumer_key
  consumer_secret = confg.consumer_secret
  access_token = confg.access_token
  access_token_secret = confg.access_token_secret
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)
  api = tweepy.API(auth)
  api.update_status(w)
  var = input("-").lower()
  clean(var, q1)


def chat(var, q1):  
  i = 0     
  y = 0                    
  num_lines = 0
  with open("conversation.txt", 'r') as f:
      for line in f:
          num_lines += 1
  for x in range(num_lines):
      try:
          keys_file = open("conversation.txt")
          lines = keys_file.readlines()
          a = lines[y].rstrip()
          if var == a:
            b = lines[y+1].rstrip()
            print(b)
            engine.say(b)
            engine.runAndWait()
            y = 0
            var = input("-").lower()
            clean(var, q1)
            y = 0
            
          else:
            y = y+2
      except IndexError: 
          pass    
  d=open("data.txt", "a")
  d.write("(" + str(currentDT) + ") " + str(i) + " i- " + str(var) +  "o- " + " .\n")
  i = i+1
  var = input("-").lower()
  clean(var, q1)

def clean(var, q1):
  b = ".!?@#$"
  for char in b:
      var = var.replace(char,"")    
  f=open("q1.txt", "r")
  q1 = f.read()  
  main(var, q1)
      

def main(var, q1):    
  if var == 'stop':
    print("i will not") 
  if var == 'password':
    password(q1)
  if var == 'learn':
    learn(q1)
  if var == q1:
    qa1(q1)
  if var == 'remember':
    remember(q1)  
  if var == "search":
    search(q1)
  if var == "translate":
    translate(q1)
  if var == "email":
    email(q1)
  if var == "tweet":
    tweet(q1)
  else:                        
    chat(var, q1)


def start():  
  var = input("Password:")
  p = confg.password
  if var == p:  
    print("Welcome sir!")
    var = input("-").lower()
    f=open("q1.txt", "r") 
    q1 = f.read()
    clean(var,q1)
  else:  
    print("Wrong password.") 
    start()

start()