

class FileOps():

    def writeListToFile(self):
        # create a list
        mylist = ['Troy', 'cymruclan@icloud.com', '50y', 'Peet\'s Coffee']
        # create and opena file for writing
        f = open("C:\\Users\\troye\\Desktop\\myinfo.txt", 'w')
        f.write(str(mylist))
        f.close()
