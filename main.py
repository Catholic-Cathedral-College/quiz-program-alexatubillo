#Ask the user what is this kind of graph
print ("You need to Identify what kind of graph it is, Please enter to see the choices and questions.")
print()

graphs = ["- line graph", "- bar graph", "- histograms", "- pie charts", "- scatterplots"]
for graph in graphs:
     print(graph)
     print()

correct = 0
wrong  = 0

graph = input("1. It is a graphical representation of data:")
if graph == "bar graph":
  print("Correct!")
  correct += 1
else:
  print ("wrong")
  wrong += 1
  print()
graph = input("2. It is a short line which is drawn on a plane connecting the pionts on x and y coordinates.")
if graph == "line graph":
  print("Correct")
  correct += 1
else:  
  print("you put the wrong graph")
  wrong += 1
  print()
graph = input("3. It is a set of points plotted on a horizontal and vertical axes.")
if graph == "scatter plots":
  print("great!")
  correct += 1
else:
  print("It is the wrong one!")
  wrong += 1
  print()
graph = input("4. It is a circular statistical graphic, which is divided into slices to illustrate numerical proportion.")
if graph == "pie charts":
   print("Good job!")
   correct += 1
else:
  print("Wrong!")
  wrong += 1
  print()
graph = input("5. It is a display of statistical information that uses rectangles to show the frequency of data items in successive numerical intervals of equal size.")
if graph == "histograms":
   print("Correct, Awesome!")
   correct += 1
else:
  print("Sorry, wrong")
  wrong += 1
  print()
#Ask the user if its true or false

print (" -true or false, Please enter to see questions.-")
print()

graph = input("6. A graph needs to have a title.")
if graph == "true":
  print("correct")
  correct += 1
else:
  print("Wrong")
  wrong += 1
graph = input("7. a graph needs to have scales and axes")
if graph == "true":
  print("correct")
  correct += 1
else:
  print("Wrong")
  wrong += 1
    
#Ask the user the thing that graph must have
print()
print ("-one thing that the graph must have, choose in the choices which is the right one please enter to see question.-")
print()

graphs = ["- title", "- line ", "- scales", "- caption", "- axes", "- odd scales", "-many colours", "-data field", "-overload information"]
for graph in graphs:
     print(graph)
     print()

graph = input("8. Give one thing that graph must have.")
if graph == "caption":
    print("you're rigth")
    correct += 1
elif graph == "axes":
   print("also correct")
   correct += 1
elif graph == "scales":
  print("You are correct!")
  correct += 1
elif graph == "title":
  print("Great!, you're correct")
  correct += 1
elif graph == "data field":
   print("Correct!!")
   correct += 1
else:
  print("wrong!")
  wrong += 1
  print()
#Ask user to add the number of the correct and wrong answers

print("This are the total number of your correct and wrong answers:")

answers = correct + wrong

#Ask user to print the total number of correct and wrong answers and questions.
print() 
print("The total number of the correct answer are:{}".format(correct))
print("The total number of the wrong answer are:{}".format(wrong))
print("The total number of the correct and wrong answers/ questions are:{}".format(answers))
print("Thank you for answering the quiz :)")                                                                      







