########################################################################
# 
#   Shafiqul Alam Khan
# 
#   ENGR 5310 Probability and Random Process Final Project
# 
#   Part II - Python Graphs: 2.5
# 
########################################################################

# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import random
import os

# 2.5.1 Create a 10x10 sparse matrix A and visualize it.
A = np.array([[11, 0, 0, 0, 2, 0, 0, 0, 0, 0],      # Create sparse matrix 
              [0, 0, 5, 0, 0, 0, 22, 0, 0, 1],
              [0, 6, 0, 1, 0, 0, 0, 0, 8, 0],
              [0, 0, 3, 0, 0, 0, 0, 1, 0, 0],
              [5, 0, 1, 0, 0, 0, 0, 0, 10, 0],
              [0, 0, 0, 7, 0, 0, 0, 0, 0, 1],
              [0, 9, 0, 0, 3, 0, 0, 2, 0, 0],
              [0, 0, 1, 0, 0, 0, 1, 0, 0, 3],
              [2, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 6, 0, 0, 0, 0, 0, 0, 0, 9]])

plt.figure(figsize=(8, 8))
plt.spy(A, precision = 0.1, markersize = 5)         # Plot sparse matrix
plt.title('2.5.1 10x10 sparse matrix')
plt.savefig('2.5.1 10x10 sparse matrix.png')          # 2.5.6 Save figures
plt.savefig('2.5.1 10x10 sparse matrix.svg')          # 2.5.6 Save figures
plt.savefig('2.5.1 10x10 sparse matrix.jpeg')         # 2.5.6 Save figures
plt.savefig('2.5.1 10x10 sparse matrix.pdf')          # 2.5.6 Save figures
plt.clf()


# 2.5.2 Create a plot that shows sine(x), cos(x) and sin(x)cos(x) on same plot.
x = np.arange(0, 5*np.pi, 0.1)      # Creating x axis and y axis
y1 = np.sin(x)
y2 = np.cos(x)
y3 = y1*y2

plt.figure(figsize=(10, 8))
plt.plot(x, y1, color='red')                        # Plot sine(x), cos(x) and sin(x)cos(x)
plt.plot(x, y2, color='blue')
plt.plot(x, y3, color='green')
plt.title('2.5.2 Plot of sine(x), cos(x) and sin(x)cos(x)')
plt.savefig('2.5.2 sine(x), cos(x) and sin(x)cos(x) plot.png')          # 2.5.6 Save figures
plt.savefig('2.5.2 sine(x), cos(x) and sin(x)cos(x) plot.svg')          # 2.5.6 Save figures
plt.savefig('2.5.2 sine(x), cos(x) and sin(x)cos(x) plot.jpeg')         # 2.5.6 Save figures
plt.savefig('2.5.2 sine(x), cos(x) and sin(x)cos(x) plot.pdf')          # 2.5.6 Save figures
plt.clf()


# 2.5.3 Create Bar chart and pie chart chart using any random data.
# Bar chart
random.seed(42)                         # Set random seed
x_bar = np.arange(10)                   # Define x 
y_bar = np.random.randint(0,20,10)      # Define y with random values

plt.figure(figsize=(10, 8))
plt.bar(x_bar, y_bar)                   # Plot bar chart
plt.xlabel('Numbers')
plt.ylabel('Values')
plt.title('2.5.3 Bar plot')
plt.savefig('2.5.3 Bar plot.png')          # 2.5.6 Save figures
plt.savefig('2.5.3 Bar plot.svg')          # 2.5.6 Save figures
plt.savefig('2.5.3 Bar plot.jpeg')         # 2.5.6 Save figures
plt.savefig('2.5.3 Bar plot.pdf')          # 2.5.6 Save figures
plt.clf()

# Pie chart
labels = ['A', 'B', 'C', 'D', 'E', 'F']     # Create random labels
data = [5, 13, 30, 23, 12, 17]              # Create random data

plt.figure(figsize=(8, 8))
plt.pie(data, labels = labels)
plt.title('2.5.3 Pie Plot')                 # Plot pie chart
plt.savefig('2.5.3 Pie plot.png')          # 2.5.6 Save figures
plt.savefig('2.5.3 Pie plot.svg')          # 2.5.6 Save figures
plt.savefig('2.5.3 Pie plot.jpeg')         # 2.5.6 Save figures
plt.savefig('2.5.3 Pie plot.pdf')          # 2.5.6 Save figures
plt.clf()


# 2.5.4 Create a histogram using random data (you may use data on Matplotlib website).
random.seed(12)                                         # Set random seed
dt = [random.randint(0, 100) for x in range(100)]       # Generate random data

plt.figure(figsize=(10, 8))
plt.hist(dt, bins=15)                                   # Plot histogram
plt.title('2.5.4 Histogram plot')
plt.savefig('2.5.4 Histogram plot.png')          # 2.5.6 Save figures
plt.savefig('2.5.4 Histogram plot.svg')          # 2.5.6 Save figures
plt.savefig('2.5.4 Histogram plot.jpeg')         # 2.5.6 Save figures
plt.savefig('2.5.4 Histogram plot.pdf')          # 2.5.6 Save figures
plt.clf()


# 2.5.5 Create a boxplot with different quantiles.
random.seed(36)                                         # Set random seed
d_1 = np.random.normal(80, 30, 250)                     # Generate random data
d_2 = np.random.normal(100, 20, 250) 
d_3 = np.random.normal(90, 50, 250) 
d_4 = np.random.normal(60, 10, 250) 
d_5 = np.random.normal(75, 35, 250)
d_6 = np.random.normal(110, 25, 250)
dt_box = [d_1, d_2, d_3, d_4, d_5, d_6]

plt.figure(figsize=(10, 8))
plt.boxplot(dt_box)
plt.title('2.5.5 Boxplot')
plt.savefig('2.5.5 Boxplot.png')          # 2.5.6 Save figures
plt.savefig('2.5.5 Boxplot.svg')          # 2.5.6 Save figures
plt.savefig('2.5.5 Boxplot.jpeg')         # 2.5.6 Save figures
plt.savefig('2.5.5 Boxplot.pdf')          # 2.5.6 Save figures
plt.clf()

# 2.5.6 Save figures with different file types (png, svg, jpeg, pdf) and compare them based on file size and scalability.
# Save figures with different file types
print('All the previous figures are saved with file types (png, svg, jpeg, pdf). \n')

# Compare them based on file size and scalability.
# 2.5.1 file sizes
f_1 = os.path.getsize('2.5.1 10x10 sparse matrix.png')
f_2 = os.path.getsize('2.5.1 10x10 sparse matrix.svg')
f_3 = os.path.getsize('2.5.1 10x10 sparse matrix.jpeg')
f_4 = os.path.getsize('2.5.1 10x10 sparse matrix.pdf')
print('2.5.1 png file size is: ', f_1, 'bytes')
print('2.5.1 svg file size is: ', f_2, 'bytes')
print('2.5.1 jpeg file size is: ', f_3, 'bytes')
print('2.5.1 pdf file size is: ', f_4, 'bytes')
print('From all the output files of 2.5.1, .svg file is the largest and .png file is the smallest.')
print('From all the output files of 2.5.1, only .svg file is scaleable. \n')

# 2.5.2 file sizes
f_1 = os.path.getsize('2.5.2 sine(x), cos(x) and sin(x)cos(x) plot.png')
f_2 = os.path.getsize('2.5.2 sine(x), cos(x) and sin(x)cos(x) plot.svg')
f_3 = os.path.getsize('2.5.2 sine(x), cos(x) and sin(x)cos(x) plot.jpeg')
f_4 = os.path.getsize('2.5.2 sine(x), cos(x) and sin(x)cos(x) plot.pdf')
print('2.5.2 png file size is: ', f_1, 'bytes')
print('2.5.2 svg file size is: ', f_2, 'bytes')
print('2.5.2 jpeg file size is: ', f_3, 'bytes')
print('2.5.2 pdf file size is: ', f_4, 'bytes')
print('From all the output files of 2.5.2, .png file is the largest and .pdf file is the smallest.')
print('From all the output files of 2.5.2, only .svg file is scaleable. \n')

# 2.5.3 file sizes
f_1 = os.path.getsize('2.5.3 Bar plot.png')
f_2 = os.path.getsize('2.5.3 Pie plot.png')
f_3 = os.path.getsize('2.5.3 Bar plot.svg')
f_4 = os.path.getsize('2.5.3 Pie plot.svg')
f_5 = os.path.getsize('2.5.3 Bar plot.jpeg')
f_6 = os.path.getsize('2.5.3 Pie plot.jpeg')
f_7 = os.path.getsize('2.5.3 Bar plot.pdf')
f_8 = os.path.getsize('2.5.3 Pie plot.pdf')
print('2.5.3 png file size is: ', f_1, 'bytes')
print('2.5.3 png file size is: ', f_2, 'bytes')
print('2.5.3 svg file size is: ', f_3, 'bytes')
print('2.5.3 svg file size is: ', f_4, 'bytes')
print('2.5.3 jpeg file size is: ', f_5, 'bytes')
print('2.5.3 jpeg file size is: ', f_6, 'bytes')
print('2.5.3 pdf file size is: ', f_7, 'bytes')
print('2.5.3 pdf file size is: ', f_8, 'bytes')
print('From all the output files of 2.5.3, .jpeg file is the largest and .pdf file is the smallest.')
print('From all the output files of 2.5.3, only .svg files are scaleable. \n')

# 2.5.4 file sizes
f_1 = os.path.getsize('2.5.4 Histogram plot.png')
f_2 = os.path.getsize('2.5.4 Histogram plot.svg')
f_3 = os.path.getsize('2.5.4 Histogram plot.jpeg')
f_4 = os.path.getsize('2.5.4 Histogram plot.pdf')
print('2.5.4 png file size is: ', f_1, 'bytes')
print('2.5.4 svg file size is: ', f_2, 'bytes')
print('2.5.4 jpeg file size is: ', f_3, 'bytes')
print('2.5.4 pdf file size is: ', f_4, 'bytes')
print('From all the output files of 2.5.4, .jpeg file is the largest and .png file is the smallest.')
print('From all the output files of 2.5.4, only .svg file is scaleable. \n')

# 2.5.5 file sizes
f_1 = os.path.getsize('2.5.5 Boxplot.png')
f_2 = os.path.getsize('2.5.5 Boxplot.svg')
f_3 = os.path.getsize('2.5.5 Boxplot.jpeg')
f_4 = os.path.getsize('2.5.5 Boxplot.pdf')
print('2.5.5 png file size is: ', f_1, 'bytes')
print('2.5.5 svg file size is: ', f_2, 'bytes')
print('2.5.5 jpeg file size is: ', f_3, 'bytes')
print('2.5.5 pdf file size is: ', f_4, 'bytes')
print('From all the output files of 2.5.5, .svg file is the largest and .pdf file is the smallest.')
print('From all the output files of 2.5.5, only .svg file is scaleable. \n')


# 2.5.7 Create and change figure titles, x and y-axis labels, grid thickness, and etc.
random.seed(40)                                         # Set random seed
dt_ln = np.random.random(100)                           # Generate random data

plt.figure(figsize=(10, 8))
plt.plot(dt_ln)                             # Plot the initial line graph
plt.xlabel('x')                             # Create x lable
plt.ylabel('y')                             # Create y label
plt.title('2.5.7 line plot')                # Create title
plt.savefig('2.5.7 line plot.png')          # Save initial plot

plt.plot(dt_ln, color='green', linewidth=4, label='Data') # Change plot color, linewidth
plt.xlabel('Datapoints')                    # Change x lable
plt.ylabel('Random Value')                  # Change y label
plt.title('2.5.7 Random Data Plot')         # Change figure title
plt.legend()                                # Add legend
plt.grid(color='blue', linestyle='-', linewidth=2)     # Add grid, change color of grid, change line width of grid
plt.savefig('2.5.7 modified line plot.png')          # Save the modified plot
plt.clf()