grid = 21

MIN_bump_slope = 0.01
MAX_bump_slope = 0.50

MIN_bump_rnorm = 0.05
MAX_bump_rnorm = 1.00

DoNodes = True
rmin = 0.1

counter = 0
for i in range(0,grid) :
	bump_slope = MIN_bump_slope + i * ( MAX_bump_slope - MIN_bump_slope ) / ( grid - 1)
	for j in range(0,grid) :
		bump_rnorm = MIN_bump_rnorm + j * ( MAX_bump_rnorm - MIN_bump_rnorm ) / ( grid - 1)
		counter += 1
		filename = "G:\\L395_BR4\\test_%05d.txt" % (counter)
		print(bump_slope, bump_rnorm)
		N3DFix_Tree( neuron[0], 0, bump_slope, bump_rnorm, rmin, DoNodes, filename )

		
	
grid = 150

MIN_bump_rnorm = 0.01
MAX_bump_rnorm = 1.50

DoNodes = True
rmin = 0.1

counter = 0
for j in range(0,grid) :
	bump_rnorm = MIN_bump_rnorm + j * ( MAX_bump_rnorm - MIN_bump_rnorm ) / ( grid - 1)
	print(bump_rnorm)
	counter += 1
	filename = "G:\\L395_BR4\\test_%05d.txt" % (counter)
	N3DFix_Tree( neuron[3], 0, bump_rnorm, rmin, DoNodes, filename )

	
	

grid = 91

MIN_bump_rnorm = 0.10
MAX_bump_rnorm = 1.00

DoNodes = True
rmin = 0.1

counter = 0
for j in range(0,grid) :
	bump_rnorm = MIN_bump_rnorm + j * ( MAX_bump_rnorm - MIN_bump_rnorm ) / ( grid - 1)
	print(bump_rnorm)
	counter += 1
	filename = "G:\\ZZZ\\test_%05d.txt" % (counter)
	N3DFix_Tree( neuron[8], 0, bump_rnorm, rmin, DoNodes, filename )

