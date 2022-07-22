import matplotlib.pyplot as plt

x_rounds = []
y_diff = []

plotting = open('NumberReport.txt', 'r')
macro = plotting.readline()
p = plotting.readline()
x = plotting.readline()
y = plotting.readline()

for line_number in range(30000):
    line = plotting.readline().split()
    x_rounds.append( int( line[ 0 ] ))
    y_diff.append( int( line[ 4 ] ) )

plt.title("Difference of Zprotocol Macropayment and the Interactive Macroppayment")
plt.xlabel('Round')
plt.ylabel('Difference')
plt.plot(x_rounds, y_diff, label="Diff of ZproMacropayment and InteractiveMacroppayment")
plt.legend( loc="upper right" )
plt.axhline(y=0, color='b', linestyle='-')
plt.savefig("Macropayment_Difference.jpg")

plt.show()

plotting.close()
