def questions(quest):
  if(quest=="how are you"):
    print("I am fine")
  elif(quest=="what are you upto"):
    print("Nothing much")
  elif(quest=="good morning"):
    print("Good morning")
  elif(quest=="tell me something"):
    print("hope you doing fine")
  elif(quest=="hi, what is your name"):
    print("ChatBot")
  elif(quest=="happy birthday"):
    print("Thank You")
  elif(quest=="who made you"):
    print("My Developer")
  elif(quest=="which languages can you speak"):
    print("English, Hindi, Marathi, Gujarati")
  elif(quest=="where do you live"):
    print("AT Home")
  elif(quest=="do you get smarter"):
    print("Every Day a bit")
  elif(quest=="what is your age"):
    print("It's not been much")
  elif(quest=="what is the weather today"):
    print("Its sunny today")
  elif(quest=="do you speak English"):
    print("Yes i do")
  elif(quest=="what is your favorite color"):
    print("Navy Blue")
  elif(quest=="let us play a game"):
    print("Ok lets play")
  elif(quest=="send an email"):
    print("Email sent")
  elif(quest=="are you a robot"):
    print("Yes I am a Robot")
  elif(quest=="what do you think about bollywood"):
    print("Its getting worse day by day")
  elif(quest=="what about indian politics"):
    print("It seems to be better")
  elif(quest=="pray for rishabh pant"):
    print("hope for his speedy recovery")
  else:
    print("Choose correct option")

q=['how are you','what are you upto','good morning','tell me something','hi, what is your name','happy birthday','who made you','which languages can you speak','where do you live','do you get smarter','what is your age','what is the weather today','do you speak English','what is your favorite color','let us play a game','send an email','are you a robot','what do you think about bollywood','what about indian politics','pray for rishabh pant']

print("Following questions to be asked")
def printquestions(q):
  for i in q:
    print(i)

printquestions(q)


i=1

while True:
  symbols = {'`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[',']','}','}','|','\'',';','"','\'','<',',','>','.','?','/'}
  mesg = input("Enter the message!! ")
  message = ""

  for i in mesg:
    if i not in symbols:
      message+=i
  print(message)

  message = message.lower()

  if (message=="stop" or message=="exit"):
    print("Thank you")
    break
  else:
    questions(message) 
    # i+=1





