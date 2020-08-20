import webbrowser
import pyttsx3
import os

pyttsx3.speak("Hello ,This is Rover your Personal Assistance")
print("Hello ,This is Jarvis your Personal Assistance ")

while True:
   print("chat with me with your requirements :- ")
   pyttsx3.speak("chat with me with your requirements :-")

   p = input()
   os.system(p)

   if 'chrome' in p:
        os.system("chrome")
        print("Here I open chrome browser for you")
        pyttsx3.speak("Here I open chrome browser for you")
         
   elif 'open youtube' in p:
        webbrowser.open("youtube.com")
        print("Here I open youtube for you")
        pyttsx3.speak("Here I open youtube for you")
        continue


   elif ('open' in p) and ('facebook' in p):
        webbrowser.open("https://www.facebook.com/")
        print("Here I open facebook for you")
        pyttsx3.speak("Here I open facebook for you")
        continue

   elif  ("exit" in p)  or ("quit" in p):
       pyttsx3.speak("Thank You,Have a nice day")
       print("Thank You Sachin, Have a nice day!!!")
       exit()
