# https://cloud.google.com/translate/docs/languages
# This is th project made by Paramdeep Singh Gill
import random
import time
import datetime
import pyglet
from gtts import gTTS
import os
import requests, sys, webbrowser, bs4
from googletrans import Translator
import sys
import subprocess as sp
import colorama
from colorama import Fore, Back, Style
import smtplib
import tweepy

currentDT = datetime.datetime.now()
i = 0
d=open("data.txt", "a")
d.write("m - Current = (")
d.write(str(currentDT))
d.write(")\n")

for x in range (0,3):
    b = "Loading" + "." * x
    print (b, end="\r")
    time.sleep(0.5)

onetosix = random.randint(1,6)
r = random.randint(1,5)
q = 1
var = input("Password:")

if var == 'p':
  
  time.sleep(0.5)
  tmp = sp.call('cls',shell=True)
  time.sleep(1)
  from sys import stdout
  def get_part_of_day(hour):
      return (
          "morning" if 5 <= hour <= 11
          else
          "afternoon" if 12 <= hour <= 17
          else
          "evening" if 18 <= hour <= 22
          else
          "night"
      )
  from datetime import datetime
  h = datetime.now().hour
  stdout.write('Good {0}! sir. \n'.format(get_part_of_day(h)))
  print("Welcome sir!")
  var = input("-")
else:
  colorama.init()
  print(Fore.RED + "Wrong password." + Style.RESET_ALL)
  var = input("Want to retry ? (y/n)")
  if var == "y":
    a = input("Password:")
    if a == "p":

      time.sleep(0.5)
      tmp = sp.call('cls',shell=True)
      time.sleep(1)
      from sys import stdout
      def get_part_of_day(hour):
          return (
              "morning" if 5 <= hour <= 11
              else
              "afternoon" if 12 <= hour <= 17
              else
              "evening" if 18 <= hour <= 22
              else
              "night"
          )
      from datetime import datetime
      h = datetime.now().hour
      stdout.write('Good {0}! sir. \n'.format(get_part_of_day(h)))
      print("Welcome sir!")
      var = input("-")
    else:
      print(Fore.RED + "Wrong password." + Style.RESET_ALL)
      time.sleep(2)
  else:
    time.sleep(2)




f=open("q1.txt", "r")
q1 = f.read()


while True:

   b = ".!?@#$"
   for char in b:
       var = var.replace(char,"")
       var = var.lower()
   if var == 'hi':
     if r == 1:
       f=open("1hi.txt", "r")
       v = f.read()
       print (v)
       m = pyglet.resource.media('1hi.mp3', streaming=False)
       m.play()
       d=open("data.txt", "a")
       d.write("(" + str(currentDT) + ") " + str(i) + " i- " + str(var) +  "o- " + str(v) + " .\n")
       var = input("-")
       if var == 'No, I donot want this reply.':
         h = input("Ok which reply do you want sir ?")
         print("Ok.")
         f=open("1hi.txt", "w")
         f.write(h)
         f.close()
         s=gTTS(h)
         s.save("1hi.mp3")
         var = input("-")
       i = i+1
       r = random.randint(1,2)
     else:
       if r == 2:
         f=open("2hi.txt", "r")
         v = f.read()
         print (v)
         m = pyglet.resource.media('2hi.mp3', streaming=False)
         m.play()
         d=open("data.txt", "a")
         d.write("(" + str(currentDT) + ") " + str(i) + " i- " + str(var) +  "o- " + str(v) + " .\n")
         var = input("-")
         if var == 'No, I donot want this reply.':
           h = input("Ok which reply do you want sir ?")
           print("Ok.")
           f=open("2hi.txt", "w")
           f.write(h)
           f.close()
           s=gTTS(h)
           s.save("2hi.mp3")
           var = input("-")
         i = i+1
         r = random.randint(1,2)
       else:
         if r == 3:
           f=open("3hi.txt", "r")
           v = f.read()
           print (v)
           m = pyglet.resource.media('3hi.mp3', streaming=False)
           m.play()
           d=open("data.txt", "a")
           d.write("(" + str(currentDT) + ") " + str(i) + " i- " + str(var) +  "o- " + str(v) + " .\n")
           var = input("-")
           if var == 'No, I donot want this reply.':
             h = input("Ok which reply do you want sir ?")
             print("Ok.")
             f=open("3hi.txt", "w")
             f.write(h)
             f.close()
             s=gTTS(h)
             s.save("3hi.mp3")
             var = input("-")
           i = i+1
           r = random.randint(1,5)
         else:
           if r == 4:
             f=open("4hi.txt", "r")
             v = f.read()
             print (v)
             m = pyglet.resource.media('4hi.mp3', streaming=False)
             m.play()
             d=open("data.txt", "a")
             d.write("(" + str(currentDT) + ") " + str(i) + " i- " + str(var) +  "o- " + str(v) + " .\n")
             var = input("-")
             if var == 'No, I donot want this reply.':
               h = input("Ok which reply do you want sir ?")
               print("Ok.")
               f=open("4hi.txt", "w")
               f.write(h)
               f.close()
               s=gTTS(h)
               s.save("4hi.mp3")
               var = input("-")
             i = i+1
             r = random.randint(1,5)
           else:
             if r == 5:
               f=open("5hi.txt", "r")
               v = f.read()
               print (v)
               m = pyglet.resource.media('5hi.mp3', streaming=False)
               m.play()
               d=open("data.txt", "a")
               d.write("(" + str(currentDT) + ") " + str(i) + " i- " + str(var) +  "o- " + str(v) + " .\n")
               var = input("-")
               if var == 'No, I donot want this reply.':
                 h = input("Ok which reply do you want sir ?")
                 print("Ok.")
                 f=open("5hi.txt", "w")
                 f.write(h)
                 f.close()
                 s=gTTS(h)
                 s.save("5hi.mp3")
                 var = input("-")
               i = i+1
               r = random.randint(1,5)
             else:
               var = input("-")
   else:
     if var == 'how are you':
       if r == 1:
         f=open("1Howareyou.txt", "r")
         v = f.read()
         print (v)
         m = pyglet.resource.media('1Howareyou.mp3', streaming=False)
         m.play()
         d=open("data.txt", "a")
         d.write("(" + str(currentDT) + ") " + str(i) + " i- " + str(var) +  "o- " + str(v) + " .\n")
         var = input("-")
         if var == 'No, I donot want this reply.':
           h = input("Ok which reply do you want sir ?")
           print("Ok.")
           f=open("1Howareyou.txt", "w")
           f.write(h)
           f.close()
           s=gTTS(h)
           s.save("1Howareyou.mp3")
           var = input("-")
         i = i+1
         r = random.randint(1,5)
       else:
         if r == 2:
           f=open("2Howareyou.txt", "r")
           v = f.read()
           print (v)
           m = pyglet.resource.media('2Howareyou.mp3', streaming=False)
           m.play()
           d=open("data.txt", "a")
           d.write("(" + str(currentDT) + ") " + str(i) + " i- " + str(var) +  "o- " + str(v) + " .\n")
           var = input("-")
           if var == 'No, I donot want this reply.':
             h = input("Ok which reply do you want sir ?")
             print("Ok.")
             f=open("2Howareyou.txt", "w")
             f.write(h)
             f.close()
             s=gTTS(h)
             s.save("2Howareyou.mp3")
             var = input("-")
           i = i+1
           r = random.randint(1,5)
         else:
           if r == 3:
             f=open("3Howareyou.txt", "r")
             v = f.read()
             print (v)
             m = pyglet.resource.media('3Howareyou.mp3', streaming=False)
             m.play()
             d=open("data.txt", "a")
             d.write("(" + str(currentDT) + ") " + str(i) + " i- " + str(var) +  "o- " + str(v) + " .\n")
             var = input("-")
             if var == 'No, I donot want this reply.':
               h = input("Ok which reply do you want sir ?")
               print("Ok.")
               f=open("3Howareyou.txt", "w")
               f.write(h)
               f.close()
               s=gTTS(h)
               s.save("3Howareyou.mp3")
               var = input("-")
             i = i+1
             r = random.randint(1,5)
           else:
             if r == 4:
               f=open("4Howareyou.txt", "r")
               v = f.read()
               print (v)
               m = pyglet.resource.media('4Howareyou.mp3', streaming=False)
               m.play()
               d=open("data.txt", "a")
               d.write("(" + str(currentDT) + ") " + str(i) + " i- " + str(var) +  "o- " + str(v) + " .\n")
               var = input("-")
               if var == 'No, I donot want this reply.':
                 h = input("Ok which reply do you want sir ?")
                 print("Ok.")
                 f=open("4Howareyou.txt", "w")
                 f.write(h)
                 f.close()
                 s=gTTS(h)
                 s.save("4Howareyou.mp3")
                 var = input("-")
               i = i+1
               r = random.randint(1,5)
             else:
               if r == 5:
                 f=open("5Howareyou.txt", "r")
                 v = f.read()
                 print (v)
                 m = pyglet.resource.media('5Howareyou.mp3', streaming=False)
                 m.play()
                 d=open("data.txt", "a")
                 d.write("(" + str(currentDT) + ") " + str(i) + " i- " + str(var) +  "o- " + str(v) + " .\n")
                 var = input("-")
                 if var == 'No, I donot want this reply.':
                   h = input("Ok which reply do you want sir ?")
                   print("Ok.")
                   f=open("5Howareyou.txt", "w")
                   f.write(h)
                   f.close()
                   s=gTTS(h)
                   s.save("5Howareyou.mp3")
                   var = input("-")
                 i = i+1
                 r = random.randint(1,5)
               else:
                 var = input("-")

     else:
       if var == 'What is your name ?':
         if r == 1:
           print("Hi.")
           r = random.randint(1,5)
           var = input("-")
         else:
           if r == 2:
             print("Hello.")
             r = random.randint(1,5)
             var = input("-")
           else:
             if r == 3:
               print("Hello Sir.")
               r = random.randint(1,5)
               var = input("-")
             else:
               if r == 4:
                 print("Hi, Sir.")
                 r = random.randint(1,5)
                 var = input("-")
               else:
                 if r == 5:
                   print("Bonjour")
                   r = random.randint(1,5)
                   var = input("-")
                 else:
                   var = input("-")
       else:
         if var == 'describe yourself':
           if q == 1:
             f=open("1describe.txt", "r")
             v = f.read()
             print (v)
             m = pyglet.resource.media('1describe.mp3', streaming=False)
             m.play()
             d=open("data.txt", "a")
             d.write("(" + str(currentDT) + ") " + str(i) + " i- " + str(var) +  "o- " + str(v) + " .\n")
             var = input("-")
             if var == 'No, I donot want this reply.':
               h = input("Ok which reply do you want sir ?")
               print("Ok.")
               f=open("1describe.txt", "w")
               f.write(h)
               f.close()
               s=gTTS(h)
               s.save("1describe.mp3")
               var = input("-")
             i = i+1
             r = random.randint(1,5)
           else:
             var = input("-")
         else:
           if var == 'stop':
             break
           else:
             if var == 'create':
               import time
               import sys
               toolbar_width = 10
               sys.stdout.write("[%s]" % (" " * toolbar_width))
               sys.stdout.flush()
               sys.stdout.write("\b" * (toolbar_width+1))
               for i in range(toolbar_width):
                   time.sleep(0.5)
                   sys.stdout.write("-")
                   sys.stdout.flush()
               sys.stdout.write("\n")
               f=open("1hi.txt","w")
               f.write("Hi.")
               f.close()
               s=gTTS("Hi.")
               s.save("1hi.mp3")
               f=open("2hi.txt","w")
               f.write("Hello.")
               f.close()
               s=gTTS("Hello.")
               s.save("2hi.mp3")
               f=open("3hi.txt","w")
               f.write("Hi, Sir.")
               f.close()
               s=gTTS("Hi, Sir.")
               s.save("3hi.mp3")
               f=open("4hi.txt","w")
               f.write("Hello, Sir.")
               f.close()
               s=gTTS("Hello, Sir.")
               s.save("4hi.mp3")
               f=open("5hi.txt","w")
               f.write("Bonjour.")
               f.close()
               s=gTTS("Bonjour.")
               s.save("5hi.mp3")
               f=open("1Howareyou.txt","w")
               f.write("Sir, I am fine How are you ?")
               f.close()
               s=gTTS("Sir, I am fine How are you ?")
               s.save("1Howareyou.mp3")
               f=open("2Howareyou.txt","w")
               f.write("Sir, I am fine.")
               f.close()
               s=gTTS("Sir, I am fine.")
               s.save("2Howareyou.mp3")
               f=open("3Howareyou.txt","w")
               f.write("Fine Sir.")
               f.close()
               s=gTTS("Fine Sir.")
               s.save("3Howareyou.mp3")
               f=open("4Howareyou.txt","w")
               f.write("Very well.")
               f.close()
               s=gTTS("Very well.")
               s.save("4Howareyou.mp3")
               f=open("5Howareyou.txt","w")
               f.write("I am fine how do you do ?")
               f.close()
               s=gTTS("I am fine how do you do ?")
               s.save("5Howareyou.mp3")
               f=open("q1.txt","w")
               f.close()
               f=open("a1.txt","w")
               f.close()
               f=open("1describe.txt","w")
               f.write("Hi, my name is P.S.Gill(Paramdeep Singh Gill). I am a chatterbot. I learn, talk, remember and much more.")
               f.close()
               s=gTTS("Hi, my name is P.S.Gill(Paramdeep Singh Gill). I am a chatterbot. I learn, talk, remember and much more.")
               s.save("1describe.mp3")
               f=open("remember.txt","w")
               f.close()
               f=open("1applause.txt","w")
               f.write("Hail, Paramdeep Singh Gill.")
               f.close()
               s=gTTS("Hail, Paramdeep Singh Gill.")
               s.save("1applause.mp3")
               s=gTTS("What do you want to search sir?")
               s.save("1search.mp3")
               s=gTTS("Do you want to open this in a browser?")
               s.save("2search.mp3")
               s=gTTS("As your wish sir.")
               s.save("3search.mp3")
               s=gTTS("What do you want to translate sir?")
               s.save("1translate.mp3")
               s=gTTS("In which language do you want to it translate sir?")
               s.save("2translate.mp3")
               s=gTTS("Done, sir.")
               s.save("1clearourchathistory.mp3")
               s=gTTS("Done, Sir.")
               s.save("1clear.mp3")
               s=gTTS("What do you want me to remember ?")
               s.save("1remember.mp3")
               s=gTTS("This is what you told me to remember last time.")
               s.save("2remember.mp3")
               s=gTTS("Ok, Sir.")
               s.save("3remember.mp3")
               s=gTTS("What is the message sir?")
               s.save("1email.mp3")
               s=gTTS("Whom you want to send this message?")
               s.save("2email.mp3")
               s=gTTS("What is the tweet sir?")
               s.save("1tweet.mp3")
               print ("Done, Sir.")
               m = pyglet.resource.media('1clear.mp3', streaming=False)
               m.play()
               var = input("-")
             else:
               if var == 'password':
                 import time
                 import sys
                 toolbar_width = 10
                 sys.stdout.write("[%s]" % (" " * toolbar_width))
                 sys.stdout.flush()
                 sys.stdout.write("\b" * (toolbar_width+1))
                 for i in range(toolbar_width):
                     time.sleep(0.3)
                     sys.stdout.write("-")
                     sys.stdout.flush()
                 sys.stdout.write("\n")
                 print("Password:")
                 time.sleep(0.1)
                 print("Gmail:")
                 time.sleep(0.1)
                 print("abcdefgh@xyz.com")
                 time.sleep(0.1)
                 print("-*********")
                 time.sleep(0.1)
                 print("abcdefgh@xyz.com")
                 time.sleep(0.1)
                 print("-********")
                 time.sleep(0.1)
                 print("Facebook:")
                 time.sleep(0.1)
                 print("abcdefgh")
                 time.sleep(0.1)
                 print("-*********")
                 time.sleep(0.1)
                 print("Linkedin:")
                 time.sleep(0.1)
                 print("abcdefgh@xyz.com")
                 time.sleep(0.1)
                 print("-********")
                 time.sleep(0.1)
                 print("Twitter:")
                 time.sleep(0.1)
                 print("abcdefgh")
                 time.sleep(0.1)
                 print("-***********")
                 time.sleep(0.1)
                 var = input("-")
               else:
                 if var == 'applause':
                   if q == 1:
                     f=open("1applause.txt", "r")
                     v = f.read()
                     print (v)
                     m = pyglet.resource.media('1applause.mp3', streaming=False)
                     m.play()
                     d=open("data.txt", "a")
                     d.write("(" + str(currentDT) + ") " + str(i) + " i- " + str(var) +  "o- " + str(v) + " .\n")
                     var = input("-")
                     if var == 'No, I donot want this reply.':
                       h = input("Ok which reply do you want sir ?")
                       print("Ok.")
                       f=open("1applause.txt", "w")
                       f.write(h)
                       f.close()
                       s=gTTS(h)
                       s.save("1applause.mp3")
                       var = input("-")
                     i = i+1
                     r = random.randint(1,5)
                   else:
                     var = input("-")
                 else:
                   if var == 'learn':
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
                     var = input("-")
                   else:
                     if var == q1:
                       f=open("a1.txt", "r")
                       v = f.read()
                       print (v)
                       var = input("-")
                     else:
                       if var == 'remember':
                         h = input("What do you want me to remember ?")
                         m = pyglet.resource.media('1remember.mp3', streaming=False)
                         m.play()
                         if h == "History.":
                           print("This is what you told me to remember last time.")
                           m = pyglet.resource.media('2remember.mp3', streaming=False)
                           m.play()
                           f=open("remember.txt", "r")
                           v = f.read()
                           print (v)
                         else:
                           f=open("remember.txt", "a")
                           f.write("\n" + h)
                           f.close()
                         print("Ok, Sir.")
                         m = pyglet.resource.media('3remember.mp3', streaming=False)
                         m.play()
                         var = input("-")
                       else:
                         if var == "clear the screen":
                           time.sleep(0.5)
                           import subprocess as sp
                           tmp = sp.call('cls',shell=True)
                           time.sleep(1)
                           var = input("-")
                         else:
                           if var == "clear our chat history":
                             f=open("data.txt","w")
                             f.close()
                             print("Done, sir.")
                             m = pyglet.resource.media('1clearourchathistory.mp3', streaming=False)
                             m.play()
                             var = input("-")
                           else:
                             if var == "search":
                               m = pyglet.resource.media('1search.mp3', streaming=False)
                               m.play()
                               var = input("What do you want to search sir?:")
                               res = requests.get('http://google.com/search?q=' + var )
                               res.raise_for_status()
                               soup = bs4.BeautifulSoup(res.text, "html.parser")
                               linkElements = soup.select('.r a')
                               print("1-->  " + str(linkElements[1]))
                               print("2-->  " + str(linkElements[2]))
                               print("3-->  " + str(linkElements[3]))
                               print("4-->  " + str(linkElements[4]))
                               m = pyglet.resource.media('2search.mp3', streaming=False)
                               m.play()
                               v = input("Do you want to open this in a browser?(y/n)")
                               if v == "y":
                                  print("As your wish sir.")
                                  m = pyglet.resource.media('3search.mp3', streaming=False)
                                  m.play()
                                  time.sleep(1)
                                  webbrowser.open('http://google.com/search?q=' + var)
                               else:
                                 var = input("-")
                             else:
                               if var == "translate":
                                 m = pyglet.resource.media('1translate.mp3', streaming=False)
                                 m.play()
                                 v = input("What do you want to translate sir?:")
                                 print("Afrikaans	af")
                                 time.sleep(0.1)
                                 print("Albanian	sq")
                                 time.sleep(0.1)
                                 print("Amharic	am")
                                 time.sleep(0.1)
                                 print("Arabic	ar")
                                 time.sleep(0.1)
                                 print("Armenian	hy")
                                 time.sleep(0.1)
                                 print("Azerbaijani	az")
                                 time.sleep(0.1)
                                 print("Basque	eu")
                                 time.sleep(0.1)
                                 print("Belarusian	be")
                                 time.sleep(0.1)
                                 print("Bengali	bn")
                                 time.sleep(0.1)
                                 print("Bosnian	bs")
                                 time.sleep(0.1)
                                 print("Bulgarian	bg")
                                 time.sleep(0.1)
                                 print("Catalan	ca")
                                 time.sleep(0.1)
                                 print("Cebuano	ceb (ISO-639-2)")
                                 time.sleep(0.1)
                                 print("Chinese (Simplified)	zh-CN (BCP-47)")
                                 time.sleep(0.1)
                                 print("Chinese (Traditional)	zh-TW (BCP-47)")
                                 time.sleep(0.1)
                                 print("Corsican	co")
                                 time.sleep(0.1)
                                 print("Croatian	hr")
                                 time.sleep(0.1)
                                 print("Czech	cs")
                                 time.sleep(0.1)
                                 print("Danish	da")
                                 time.sleep(0.1)
                                 print("Dutch	nl")
                                 time.sleep(0.1)
                                 print("English	en")
                                 time.sleep(0.1)
                                 print("Esperanto	eo")
                                 time.sleep(0.1)
                                 print("Estonian	et")
                                 time.sleep(0.1)
                                 print("Finnish	fi")
                                 time.sleep(0.1)
                                 print("French	fr")
                                 time.sleep(0.1)
                                 print("Frisian	fy")
                                 time.sleep(0.1)
                                 print("Galician	gl")
                                 time.sleep(0.1)
                                 print("Georgian	ka")
                                 time.sleep(0.1)
                                 print("German	de")
                                 time.sleep(0.1)
                                 print("Greek	el")
                                 time.sleep(0.1)
                                 print("Gujarati	gu")
                                 time.sleep(0.1)
                                 print("Haitian Creole	ht")
                                 time.sleep(0.1)
                                 print("Hausa	ha")
                                 time.sleep(0.1)
                                 print("Hawaiian	haw (ISO-639-2)")
                                 time.sleep(0.1)
                                 print("Hebrew	he**")
                                 time.sleep(0.1)
                                 print("Hindi	hi")
                                 time.sleep(0.1)
                                 print("Hmong	hmn (ISO-639-2)")
                                 time.sleep(0.1)
                                 print("Hungarian	hu")
                                 time.sleep(0.1)
                                 print("Icelandic	is")
                                 time.sleep(0.1)
                                 print("Igbo	ig")
                                 time.sleep(0.1)
                                 print("Indonesian	id")
                                 time.sleep(0.1)
                                 print("Irish	ga")
                                 time.sleep(0.1)
                                 print("Italian	it")
                                 time.sleep(0.1)
                                 print("Japanese	ja")
                                 time.sleep(0.1)
                                 print("Javanese	jw")
                                 time.sleep(0.1)
                                 print("Kannada	kn")
                                 time.sleep(0.1)
                                 print("Kazakh	kk")
                                 time.sleep(0.1)
                                 print("Khmer	km")
                                 time.sleep(0.1)
                                 print("Korean	ko")
                                 time.sleep(0.1)
                                 print("Kurdish	ku")
                                 time.sleep(0.1)
                                 print("Kyrgyz	ky")
                                 time.sleep(0.1)
                                 print("Lao	lo")
                                 time.sleep(0.1)
                                 print("Latin	la")
                                 time.sleep(0.1)
                                 print("Latvian	lv")
                                 time.sleep(0.1)
                                 print("Lithuanian	lt")
                                 time.sleep(0.1)
                                 print("Luxembourgish	lb")
                                 time.sleep(0.1)
                                 print("Macedonian	mk")
                                 time.sleep(0.1)
                                 print("Malagasy	mg")
                                 time.sleep(0.1)
                                 print("Malay	ms")
                                 time.sleep(0.1)
                                 print("Malayalam	ml")
                                 time.sleep(0.1)
                                 print("Maltese	mt")
                                 time.sleep(0.1)
                                 print("Maori	mi")
                                 time.sleep(0.1)
                                 print("Marathi	mr")
                                 time.sleep(0.1)
                                 print("Mongolian	mn")
                                 time.sleep(0.1)
                                 print("Myanmar (Burmese)	my")
                                 time.sleep(0.1)
                                 print("Nepali	ne")
                                 time.sleep(0.1)
                                 print("Norwegian	no")
                                 time.sleep(0.1)
                                 print("Nyanja (Chichewa)	ny")
                                 time.sleep(0.1)
                                 print("Pashto	ps")
                                 time.sleep(0.1)
                                 print("Persian	fa")
                                 time.sleep(0.1)
                                 print("Polish	pl")
                                 time.sleep(0.1)
                                 print("Portuguese (Portugal, Brazil)	pt")
                                 time.sleep(0.1)
                                 print("Punjabi	pa")
                                 time.sleep(0.1)
                                 print("Romanian	ro")
                                 time.sleep(0.1)
                                 print("Russian	ru")
                                 time.sleep(0.1)
                                 print("Samoan	sm")
                                 time.sleep(0.1)
                                 print("Scots Gaelic	gd")
                                 time.sleep(0.1)
                                 print("Serbian	sr")
                                 time.sleep(0.1)
                                 print("Sesotho	st")
                                 time.sleep(0.1)
                                 print("Shona	sn")
                                 time.sleep(0.1)
                                 print("Sindhi	sd")
                                 time.sleep(0.1)
                                 print("Sinhala (Sinhalese)	si")
                                 time.sleep(0.1)
                                 print("Slovak	sk")
                                 time.sleep(0.1)
                                 print("Slovenian	sl")
                                 time.sleep(0.1)
                                 print("Somali	so")
                                 time.sleep(0.1)
                                 print("Spanish	es")
                                 time.sleep(0.1)
                                 print("Sundanese	su")
                                 time.sleep(0.1)
                                 print("Swahili	sw")
                                 time.sleep(0.1)
                                 print("Swedish	sv")
                                 time.sleep(0.1)
                                 print("Tagalog (Filipino)	tl")
                                 time.sleep(0.1)
                                 print("Tajik	tg")
                                 time.sleep(0.1)
                                 print("Tamil	ta")
                                 time.sleep(0.1)
                                 print("Telugu	te")
                                 time.sleep(0.1)
                                 print("Thai	th")
                                 time.sleep(0.1)
                                 print("Turkish	tr")
                                 time.sleep(0.1)
                                 print("Ukrainian	uk")
                                 time.sleep(0.1)
                                 print("Urdu	ur")
                                 time.sleep(0.1)
                                 print("Uzbek	uz")
                                 time.sleep(0.1)
                                 print("Vietnamese	vi")
                                 time.sleep(0.1)
                                 print("Welsh	cy")
                                 time.sleep(0.1)
                                 print("Xhosa	xh")
                                 time.sleep(0.1)
                                 print("Yiddish	yi")
                                 time.sleep(0.1)
                                 print("Yoruba	yo")
                                 time.sleep(0.1)
                                 print("Zulu	zu")
                                 time.sleep(0.1)
                                 m = pyglet.resource.media('2translate.mp3', streaming=False)
                                 m.play()
                                 w = input("In which language do you want to it translate sir?:")
                                 translator = Translator()
                                 k = translator.translate(v, dest=w)
                                 print(k)
                                 var = input("-")
                               else:
                                 if var == "email.":
                                   m = pyglet.resource.media('1email.mp3', streaming=False)
                                   m.play()
                                   w = input("What is the message sir?")
                                   m = pyglet.resource.media('2email.mp3', streaming=False)
                                   m.play()
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
                                   var = input("-")
                                 else:
                                   if var == "tweet":
                                     m = pyglet.resource.media('2tweet.mp3', streaming=False)
                                     m.play()
                                     w = input("What is the tweet sir?")
                                     consumer_key = "sowy6hCPWcYmabLlJlDf4FzFr"
                                     consumer_secret = "WgpVYsX8FoKajamHkkxnFcLnJjlJgpJ1u8GZcubPTJbcoTLhnH"
                                     access_token = "1089739186373095424-74hb6OdXOP5hb2qNZm3YwAxbJfDxnf"
                                     access_token_secret = "L7IURXT7F82ILfP9JC7PnMtPproeCllYaw9WBwjxkMc0N"
                                     auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                                     auth.set_access_token(access_token, access_token_secret)
                                     api = tweepy.API(auth)
                                     api.update_status(w)
                                     var = input("-")
                                   else:
                                     d=open("data.txt", "a")
                                     d.write("(" + str(currentDT) + ") " + str(i) + " i- " + str(var) +  "o- " + " .\n")
                                     var = input("-")
                                     i = i+1
