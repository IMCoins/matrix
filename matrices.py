class Matrix:
	def __init__(self, matrix):
		self.matrix = matrix

	def __str__(self):
		message = '(\n'
		for line in self.matrix:
			message += '[' + str(line) + ']\n'
		message += ')'
		return message
		# return str([line for line in self.matrix])

	def scalar_multiplication(self, number):
		ret = []
		for lines in self.matrix:
			ret.append([0 for rows in self.matrix[0]])

		for i in range(len(self.matrix)):
			for j in range(len(self.matrix[0])):
				ret[i][j] = number * self.matrix[i][j]

		return Matrix(ret)

	def matrix_multiplication(self, other_matrix):
		if (len(self.matrix[0]) != len(other_matrix.matrix)):
			raise ValueError("Impossible multiplication since lines of the first matrix does\
				 not match rows of second matrix, {} {}".format(len(self.matrix),
				 												len(other_matrix.matrix[0])))

		ret = []
		for lines in self.matrix:
			ret.append([0 for rows in other_matrix.matrix[0]])

		for i in range(len(self.matrix)):
			for j in range(len(other_matrix.matrix[0])):
				for k in range(len(other_matrix.matrix)):
					ret[i][j] += self.matrix[i][k] * other_matrix.matrix[k][j]

		return Matrix(ret)

	def determinant(self):
		if (len(self.matrix) != 2 and len(self.matrix[0]) != 2):
			raise 'Matrix is not a 2x2 matrix.'
		return (self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0])

	def inverse_matrix(self):
		if (self.determinant() == 0):
			raise ValueError('Matrix is singular')
		elif (len(self.matrix) == 2 and len(self.matrix[0]) == 2):
			return Matrix([[self.matrix[1][1], -(self.matrix[0][1])],
			[-(self.matrix[1][0]), self.matrix[0][0]]]).scalar_multiplication(1. / self.determinant())
		elif (len(self.matrix) != 2 and len(self.matrix[0]) != 2):
			raise ValueError('This class can only perform 2x2 matrix inversion at the moment.')

	"""	Pour resoudre un systeme, e.g:
		3x + 2y = 0
		2x - 5y = 3
		On transforme ca en matrice, on prend la matrice inverse de notre membre de gauche,
		et on fait une multiplication matricielle entre le resultat et la matrice inverse
		precedemment preparee.
	"""

if __name__ == '__main__':
	m1 = Matrix([[1, 2],
				  [3, 4]])

	m2 = Matrix([[6],
				 [2]])

	print 'Matrix m1:', m1
	print 'Matrix m2:', m2

	print 'm1*m2:', m1.matrix_multiplication(m2)

	m3 = Matrix([[31, 4],
				 [-5, 2]])

	print 'determinant:', m3.determinant()

	m4 = Matrix([[-4, 0],
				 [-10, -6]])

	print m4.determinant()
	print 0.16666666666666666 * 6
	inv_m4 = m4.inverse_matrix()
	print 'inverse:', inv_m4
	print m4.matrix_multiplication(inv_m4)