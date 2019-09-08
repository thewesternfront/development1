
import math

def main():

    vector_a = [1, 0]
    vector_b = [0, 1]
    vector_rad = [abs(1/math.sqrt(2)), abs(1/math.sqrt(2))]
    pythag = [3, 4, 5]

    normalizeVector(vector_a)
    normalizeVector(vector_b)
    normalizeVector(vector_rad)
    normalizeVector(pythag)

def normalizeVector(vectora):

    accumulate = 0
    for item in vectora:
        accumulate = accumulate + abs(item)**2
    print(int(round(accumulate)))


if __name__ == '__main__':
    main()