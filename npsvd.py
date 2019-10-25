import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

la = np.linalg
words = ["I", "like", "enjoy", "deep", "learning", "NLP", "flying", "."]
X = np.array([
	[0, 2, 1, 0, 0, 0, 0, 0], 
	[2, 0, 0, 1, 0, 1, 0, 0], 
	[1, 0, 0, 0, 0, 0, 1, 0], 
	[0, 1, 0, 0, 1, 0, 0, 0], 
	[0, 0, 0, 1, 0, 0, 0, 1], 
	[0, 1, 0, 0, 0, 0, 0, 1], 
	[0, 0, 1, 0, 0, 0, 0, 1], 
	[0, 0, 0, 0, 1, 1, 1, 0], 
	])

U, s, Vh = la.svd(X, full_matrices=False)

plt.xticks(np.linspace(-1, 1, 10))
plt.yticks(np.linspace(-1, 1, 10))

for i in range(len(words)):
	#print("%f %f" %(U[i, 0], U[i, 1]))
	plt.text(U[i, 0], U[i, 1], words[i])

plt.show()
plt.savefig('co-matrix.png')