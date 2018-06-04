#1/usr/bin/python2.7
import matplotlib.pyplot as plt

def drawLine():
  x = [1, 2, 3]     # x axis values
  y = [10, 20, 30]  # y axis values

  plt.plot(x, y, label = 'line 1')    # plotting the points

  plt.xlabel('x - axis')  # naming x axis
  plt.ylabel('y - axis')  # naming y axis
  
  plt.title('Line Graph') # giving title to a graph

  plt.show()  # function to show the plot

if __name__ == '__main__':
  drawLine()
