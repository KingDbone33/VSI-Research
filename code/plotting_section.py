import matplotlib.pyplot as plt

x_rounds = []
y_macro = []
y_micro = []

plotting = open('NumberReport.txt', 'r')
macro = plotting.readline()
p = plotting.readline()
x = plotting.readline()
y = plotting.readline()

for line_number in range(3000):
    line = plotting.readline().split()
    x_rounds.append( line[ 0 ] )
    y_micro.append( float( line[ 1 ] ) )
    y_macro.append( float( line[ 2 ] ) )

plt.title("Micropayment vs Macropayment")
plt.xlabel('Round')
plt.ylabel('Cumulative Payment Value')
plt.plot(x_rounds, y_micro, label="Micropayment")
plt.plot(x_rounds, y_macro, label="Macropayment")
plt.legend( loc="upper right" )
  
plt.show()

plotting.close()
