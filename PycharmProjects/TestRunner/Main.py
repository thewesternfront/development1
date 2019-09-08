import csv
from enum import Enum




class Instructions(Enum):

    ENVIRONMENT=0
    CLASS=1
    SERVICE=2
    ACTION=3
    PROPERTIES=4



    def __init__(self):
        print("test instructions")







class TestRunner:

    def __init__(self):
        print("test runner")







    def RunFixedFile(self):

        services = []
        data = list()
        matrix_reader = csv.reader(open('tests.csv', 'rb'), delimiter=',', quotechar='"')
        for row_index, row in enumerate(matrix_reader):
            for item_index, item in enumerate(row):
                if len(data) <= item_index:
                    data.append([])
                data[item_index].append(item)
                #if(item_index == 3):

                # could also switch these 2 following lines to print all items in the list
                if (item_index == Instructions.ACTION):
                    services.append(item)
                    print("Service Action is " + item)
                    print(services[row_index])

# Try enum like SERVICEACTION = 1 so services[SERVICEACTION] retrieves "stop"





    def RunTest(self):

        print("This is the method")


        data = list(csv.reader(open("tests.csv")))
        #print data[1][3]

        for i, x in enumerate(data):
            print (x[0], x[1], x[2], x[3], x[4])


        environment_name = x[0]
        class_name = x[1]
        service_name = x[2]
        service_action = x[3]
        property_file = x[4]

        print("The Service Name is " + service_name)



def main():

    tr = TestRunner()
    #tr.RunTest()
    tr.RunFixedFile()


if __name__ == '__main__':
    main()




