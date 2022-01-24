# https://cloud.google.com/translate/docs/languages
# This project is made by Paramdeep Singh Gill


import time
import datetime
from gtts import gTTS
import os
import requests, sys, webbrowser, bs4
from googletrans import Translator
import subprocess as sp
import tweepy
import confg
import pyttsx3
engine = pyttsx3.init()

currentDT = datetime.datetime.now()
d=open("data.txt", "w")
d.write("m - Current = (" + str(currentDT) + ")\n")

for x in range(3):
  print('-', flush=True, end="")
  time.sleep(0.5)
print("\n")



def password():
  for x in range(5):
    time.sleep(1)
    print("-", flush=True, end='')
  f=open("password.txt", "r")
  v = f.read()
  print(v)
  var = input("-").lower()
  clean(var)

def learn():
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
  clean(var)
  f=open("q1.txt", "r")
  q1 = f.read()

def q1():
  f=open("a1.txt", "r")
  var = f.read()
  print(var)
  engine.say(var)
  engine.runAndWait()
  var = input("-").lower()
  clean(var)

def remember():
  h = input("What do you want me to remember ?")
  engine.say("TWhat do you want me to remember ?")
  engine.runAndWait()
  if h == "History.":
    print("This is what you told me to remember last time.")
    engine.say("This is what you told me to remember last time.")
    engine.runAndWait()
    f=open("remember.txt", "r")
    var = f.read()
    print(var)
    var = input("-").lower()
    clean(var)
  else:
    f=open("remember.txt", "a")
    f.write("\n" + h)
    f.close()
    print("Ok, Sir.")
    engine.say("Ok, Sir.")
    engine.runAndWait()
    var = input("-").lower()
    clean(var)

def clear_the_screen():
  print("I will not sir")

def clear_our_chat_history():
  f=open("data.txt","w")
  f.close()
  print("Done, sir.")
  engine.say("Done, sir.")
  engine.runAndWait()
  var = input("-")
  clean(var)

def search():
  engine.say("What do you want to search sir?")
  engine.runAndWait()
  var = input("What do you want to search sir?:")
  res = requests.get('http://google.com/search?q=' + var )
  res.raise_for_status()
  soup = bs4.BeautifulSoup(res.text, "html.parser")
  linkElements = soup.select('.r a')
  print("1-->  " + str(linkElements[1]))
  print("2-->  " + str(linkElements[2]))
  print("3-->  " + str(linkElements[3]))
  print("4-->  " + str(linkElements[4]))
  engine.say("Do you want to open this in a browser?(y/n)")
  engine.runAndWait()
  v = input("Do you want to open this in a browser?(y/n)")
  if v == "y":
    print("As your wish sir.")
    engine.say("As your wish sir.")
    engine.runAndWait()
    time.sleep(1)
    webbrowser.open('http://google.com/search?q=' + var)
    var = input("-").lower()
    clean(var)
  else:
    var = input("-").lower()
    clean(var)

def translate():
  engine.say("What do you want to translate sir?:")
  engine.runAndWait()
  v = input("What do you want to translate sir?:")

  
  engine.say("In which language do you want to it translate sir?:")
  engine.runAndWait()
  w = input("In which language do you want to it translate sir?:")
  translator = Translator()
  k = translator.translate(v, dest=w)
  print(k)
  var = input("-").lower()
  clean(var)

def email():
  engine.say("What is the message sir?")
  engine.runAndWait()
  w = input("What is the message sir?")
  engine.say("Whom you want to send this message?")
  engine.runAndWait()
  n = input("Whom you want to send this message?")
  if n == 'me':
    receiver_email = 'psgillbot@gmail.com'
  else:
    receiver_email = str(n)
  myemail = 'psgillbot@gmail.com'
  server = smtplib.SMTP('smtp.gmail.com',587)
  server.starttls()
  server.login(myemail, 'param@1234')
  message = str(w)
  server.sendmail(myemail, receiver_email, message)
  server.quit()
  var = input("-").lower()
  clean(var)

def tweet():
  engine.say("What is the tweet sir?")
  engine.runAndWait()
  w = input("What is the tweet sir?")
  consumer_key = "sowy6hCPWcYmabLlJlDf4FzFr"
  consumer_secret = "WgpVYsX8FoKajamHkkxnFcLnJjlJgpJ1u8GZcubPTJbcoTLhnH"
  access_token = "1089739186373095424-74hb6OdXOP5hb2qNZm3YwAxbJfDxnf"
  access_token_secret = "L7IURXT7F82ILfP9JC7PnMtPproeCllYaw9WBwjxkMc0N"
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)
  api = tweepy.API(auth)
  api.update_status(w)
  var = input("-").lower()
  clean(var)


def chat(var):  
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
            clean(var)
            y = 0
            
          else:
            y = y+2
      except IndexError: 
          pass    
  d=open("data.txt", "a")
  d.write("(" + str(currentDT) + ") " + str(i) + " i- " + str(var) +  "o- " + " .\n")
  i = i+1
  var = input("-").lower()
  clean(var)

def clean(var):
  b = ".!?@#$"
  for char in b:
      var = var.replace(char,"")      
  main(var)
      

def main(var):  
  
  if var == 'stop':
    print("i will not")
  else:
    if var == 'password':
     password()
    else:
      if var == 'learn':
       learn()
      else:
       if var == q1:
         q1()
       else:
         if var == 'remember':
           remember()
         else:
           if var == "clear the screen":
             clear_the_screen()
           else:
             if var == "clear our chat history":
               clear_our_chat_history()
             else:
               if var == "search":
                 search()
               else:
                 if var == "translate":
                   translate()
                 else:
                   if var == "email":
                     email()
                   else:
                      if var == "tweet":
                        tweet()
                      else:                        
                        chat(var)


def start():  
  var = input("Password:")
  p = confg.password
  if var == p:  
    print("Welcome sir!")
    var = input("-").lower()
    clean(var)
  else:  
    print("Wrong password.") 
    start()
start()