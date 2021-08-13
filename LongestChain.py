

class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix
        self.numRow = len(matrix)
        self.numCol = len(matrix[0])
        self.neighbours = [[0,1], [0, -1], [1, 0], [-1, 0]]

    def LongestPath(self):

        maxPath = []
        pathDict = {}
        eleCount = 0
        for i in range(self.numRow):
            for j in range(self.numCol):
                eleCount += 1

                print("current cell: ", eleCount,"----" , i, j,"----", self.matrix[i][j])
                curRow, curCol = i, j
                count = 0
                curPath = []
                curRow, curCol = i, j
                while curRow != -1 and curCol != -1:
                    if count == self.numRow * self.numCol:
                        break
                    count += 1

                    curPath.append(self.matrix[curRow][curCol])
                    if self.matrix[curRow][curCol] in pathDict:
                        curPath.extend(pathDict[self.matrix[curRow][curCol]][1::])
                        break
                    else:
                        curRow, curCol = self.nextNeighbour(self.matrix, curRow, curCol)
                print(curPath)
                pathDict[self.matrix[i][j]] = curPath
                if len(curPath) > len(maxPath):
                    maxPath = curPath
                if len(maxPath) > self.numCol*self.numRow - (eleCount):
                    print(maxPath)
                    return len(maxPath)

        print(maxPath)
        return len(maxPath)
        
    def nextNeighbour(self, matrix, i, j): 
        for dx, dy in self.neighbours:
            if i+dx > -1 and i+dx < self.numRow and j+dy> -1 and j+dy < self.numCol:
                if self.matrix[i+dx][j+dy] == self.matrix[i][j] + 1:
                    return i+dx, j+dy
            
        
        return -1, -1

        return MaxLen
    
    def printMatrix(self):
        for row in range(self.numRow):
                print (self.matrix[row])

def main():

    a = [
        [1, 3, 8, 9],
        [4, 6, 7, 10],
        [5, 2, 12, 11],
        [16, 15, 13,14]
        ]
    mat = Matrix(a)
    mat.printMatrix()
    print("longest path lenght:", mat.LongestPath())


if __name__ == "__main__":
    main()