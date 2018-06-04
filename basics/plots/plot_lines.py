#1/usr/bin/python2.7
import matplotlib.pyplot as plt

def drawLine():
  x1 = [1, 1, 5, 5]  # x axis values
  y1 = [0, 2, 2, 0]  # y axis values

  plt.plot(x1, y1, label = 'line 1')    # plotting the points

  x2 = [1,  2,  3]  # x axis values
  y2 = [9, 19, 29]  # y axis values

  plt.plot(x2, y2, label = 'line 2')    # plotting the points

  plt.xlabel('x - axis')  # naming x axis
  plt.ylabel('y - axis')  # naming y axis
  
  plt.title('Two Lines on same Graph') # giving title to a graph

  plt.legend() # show legend on the plot

  plt.show()  # function to show the plot

if __name__ == '__main__':
  drawLine()
