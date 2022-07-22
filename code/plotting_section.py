import matplotlib.pyplot as plt

x_rounds = []
y_macro = []
y_micro = []
y_macro_int = []

plotting = open('NumberReport.txt', 'r')
macro = plotting.readline()
p = plotting.readline()
x = plotting.readline()
y = plotting.readline()

for line_number in range(30000):
    line = plotting.readline().split()
    x_rounds.append( int( line[ 0 ] ) + 1 )
    y_micro.append( float( line[ 1 ] ) )
    y_macro.append( float( line[ 2 ] ) )
    y_macro_int.append( float( line[ 3 ] ) )

plt.title("Micropayment vs Macropayment")
plt.xlabel('Round')
plt.ylabel('Cumulative Payment Value')
plt.plot(x_rounds, y_micro, label="Micropayment")
plt.plot(x_rounds, y_macro, label="ZProtocol Macropayment")
plt.plot(x_rounds, y_macro_int, label="Interactive Macropayment")
plt.legend( loc="upper right" )
plt.savefig("Win_Results.jpg")

plt.show()

plotting.close()
