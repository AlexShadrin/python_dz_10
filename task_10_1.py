class Matrix:
    def __init__(self, input_data):
        self.input = input_data
    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.input])
    def __add__(self, other):
        answer = ''
        if len(self.input) == len(other.input):
            for line_1, line_2 in zip(self.input, other.input):
                if len(line_1) != len(line_2):
                    return 'Problems with shape'
                summed_line = [x + y for x, y in zip(line_1, line_2)]
                answer += ' '.join(map(str, summed_line)) + '\n'
        else:
            return 'Problems with shape'
        return answer
matrix_1 = Matrix([[31, 22], [37, 43], [51, 86]])
matrix_2 = Matrix([[3, 5], [8, 3], [7, 1]])
print(matrix_1)
print()
print(matrix_1 + matrix_2)