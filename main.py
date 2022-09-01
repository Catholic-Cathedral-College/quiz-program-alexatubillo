#Ask the user what is this kind of graph
correct = 0
wrong  = 0

graph = input("It is a graphical representation of data:")
if graph == "bar graph":
  print("Correct!")
  correct += 1
else:
  print ("wrong")
  wrong += 1
graph = input("It is a short line which is drawn on a plane connecting the pionts on x and y coordinates.")
if graph == "line graph":
  print("Correct")
  correct += 1
else:
  print("you put the wrong graph")
  wrong += 1
graph = input("It is a set of points plotted on a horizontal and vertical axes.")
if graph == "scatter plots":
  print("great!")
  correct += 1
else:
  print("It is the wrong one!")
  wrong += 1
  graph = input("It is a circular statistical graphic, which is divided into slices to illustrate numerical proportion.")
if graph == "pie charts":
   print("Good job!")
   correct += 1
else:
  print("Wrong!")
  wrong += 1
graph = input("It is a display of statistical information that uses rectangles to show the frequency of data items in successive numerical intervals of equal size.")
if graph == "histograms":
   print("Correct, Awesome!")
   correct += 1
else:
  print("you should study the meanings of the different graphs")
  wrong += 1

#Ask the user if its true or false
graph = input("A graph needs to have a title.")
if graph == "true":
  print("correct")
  correct += 1
elif graph == "false":
    print("Wrong")
    wrong += 1
graph = input("a graph needs to have scales and axes")
if graph == "true":
  print("correct")
  correct += 1
elif graph == "false":
    print("Wrong")
    wrong += 1

#Ask the user the thingt that graph must have
graph = input("What are the things that graph must have?")
if graph == "caption":
    print("you're rigth")
    correct += 1
elif graph == "axes":
   print("also correct")
   correct += 1
elif graph == "scales":
  print("You are correct!")
  correct += 1
elif graph == "symbols":
  print("Great!, you're correct")
  correct += 1
elif graph == "data field":
   print("Correct!!")
   correct += 1
else:
  print("wrong!")
  wrong += 1

#Ask user to add the number of the people who got correct and wrong
correct += 1
wrong += 1
answers = correct + wrong

#Ask user to print the total number of people who answer
print("The people who answer the quiz are:{}".format(answers))

#print some math statements
print("5 x 2 ={}".format(5 * 2))
print("5 + 7 - 2 ={}".format(5 + 7 - 2))
print("2 ** 6 + 9 ={}".format(2 ** 6 + 9))
print("6 / 2 + 7 ={}".format(6 / 2 + 7))
print("3 ** 9 ={}".format(3 ** 9))

