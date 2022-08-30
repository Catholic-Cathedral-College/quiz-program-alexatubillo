#Ask the user what is this kind of graph

graph = input("It is a graphical representation of data:")
if graph == "bar graph":
  print("Correct!")
else:
  print ("wrong")
graph = input("It is a short line which is drawn on a plane connecting the pionts on x and y coordinates.")
if graph == "line graph":
  print("Correct")
else:
  print("you put the wrong graph")
graph = input("It is a set of points plotted on a horizontal and vertical axes.")
if graph == "scatter plots":
  print("great!")
else:
  print("It is the wrong one!")
  graph = input("It is a circular statistical graphic, which is divided into slices to illustrate numerical proportion.")
if graph == "pie charts":
   print("Good job!")
else:
  ("Wrong!")
graph = input("It is a display of statistical information that uses rectangles to show the frequency of data items in successive numerical intervals of equal size.")
if graph == "histograms":
   print("Correct, Awesome!")
else:
  print("you should study the meanings of the different graphs")

#Ask the user if its true or false
graph = input("Bargraph is a graphical representation of data")
if graph == "true":
    print("correct")
  
       

  #Ask the user to add the people who got correct and wrong answers to find how many people answers the quiz.
correct = 16
wrong  = 9

answers = correct + wrong

# print how many people answers the quiz
print("The people who answer the quiz are:{}".format(answers))

#print some math statements
print("5 x 2 ={}".format(5 * 2))
print("5 + 7 - 2 ={}".format(5 + 7 - 2))
print("2 ** 6 + 9 ={}".format(2 ** 6 + 9))
print("6 / 2 + 7 ={}".format(6 / 2 + 7))
print("3 ** 9 ={}".format(3 ** 9))

