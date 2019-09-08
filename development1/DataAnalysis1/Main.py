
import pandas as pd
import numpy as np


def main():
    print("Data Analysis")
    #createArray()
    #createZerosArray()
    #createSkipArray()
    #createSeries()
    #createDataFrame()
    readCSVFile()
    writeCSVFile()
    readHTMLFile()


def readHTMLFile():
    ranking = pd.read_html("https://www.meccanismocomplesso.org/en/meccanismo-complesso-sito-2/classifica-punteggio/")
    print(ranking[0])



def readCSVFile():
    print("Reading a CSV File into a DataFrame")
    csvframe=pd.read_csv('ch05_01.csv')
    print(csvframe)
    print("= = = = = = = = = = \n")
    csvframe=pd.read_csv('ch05_03.csv')
    print(csvframe)
    print("= = = = = = = = = = \n")
    csvframe=pd.read_csv('ch05_03.csv', index_col=['color', 'status'])
    print(csvframe)
    print("= = = = = = = = = = \n")

def writeCSVFile():
    print("Writing a CSV File from a DataFrame")
    frame=pd.DataFrame(np.arange(16).reshape((4,4)), index=['red', 'blue', 'yellow', 'white'],
                                                     columns = ['ball', 'pen', 'pencil', 'paper'])
    frame.to_csv('ch05_07.csv')
    print(frame)


def createDataFrame():
    print("Creating a Data Frame from Dictionaries")
    data = {'color': ['Orange', 'Red', 'Aqua', 'Teal'],
            'object': ['BMW', 'Barchetta', 'Gemstone', 'Seahorse'],
            'price': [40000, 70000, 2000, 200]}
    frame = pd.DataFrame(data)
    print(frame)

    frame2 = pd.DataFrame(data, columns= ['object', 'color'])
    print(frame2)
    print("These are the frame columns")
    print(frame.columns)
    print("These are the frame indexes")
    print(frame.index)
    print("These are the frame values")
    print(frame.values)


def createSeries():
    s = pd.Series( [11, 22, 33, 44], index=['a', 'b', 'c', 'd'] )
    print(s)
    print(s.index)
    print(s.values)
    print(s[1])
    print(s['b'])
    print(s[0:3])

    # Create a numpy array and then make a pandas series out of it
    arr = np.array( [111, 222, 333, 444])
    s = pd.Series(arr)
    print(s)
    print(s[s > 300])
    t = s/2
    print(t)

    z = np.log(s)
    print(z)

    print(np.sin(90))
    print(np.sin(90))

    mydict = {'red': 2000, 'blue': 1000, 'yellow': 500, 'orange': 1000}
    dser = pd.Series(mydict)
    print(dser)


    s = pd.Series( [11, 22, 33, 44], index=['a', 'b', 'c', 'd'] )
    t = pd.Series( [2, 2, 2, 2], index=['a', 'b', 'c', 'e'])
    res = s*t
    print(res)




def createArray():
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=complex)
    print(a)
    print(type(a))
    print(a.dtype)
    # the shape
    print(a.ndim)
    print(a.size)
    print(a.shape)
    print(a.itemsize)
    print(a.data)



def createZerosArray():
    za = np.zeros((5, 5))
    print(za)
    oa = np.ones((5, 5))
    print(oa)



def createSkipArray():
    sa = np.arange(2, 30, 4)
    print(sa)
    # multiply whole array content by 5
    print(sa * 5)



if __name__ == '__main__':
    main()