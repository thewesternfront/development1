

class DataStructures():
    print("Using 4 different types of Data Structures")


    def setupFourDs(self):

        # Creating 2 lists
        print("Creating 2 lists of musical instruments and musical genres")
        instruments = ['guitar', 'bass', 'cello', 'mandolin']
        genres = ['baroque', 'metal', 'djent', "celtic"]
        print(instruments)
        print(genres)


        # creating 2 tuples
        # In Python, tuples are immutable, and "immutable" means the value cannot change
        tinstruments = ('guitar', 'bass', 'cello', 'mandolin')
        tgenres = ('baroque', 'metal', 'djent', "celtic")
        tinstcategories = ('string', 'wind', 'woodwinds', 'brass', 'electric', 'folk', 'acoustic')
        print(tinstruments)
        print(tgenres)
        print(tinstcategories)


        # create a dictionary
        number_of_strings = {'Cello': 4, 'Bass': 5, 'Mandolin': 8, 'Guitar': 7}


        # create a set
        myset = {"Troy", "cymruclan@icloud.com", 50, tinstruments, tinstcategories}
        print(myset)


        ### Now to create a large list and make a set out of it ...
        ### Steps ... use a for loop to create an appendable list.
        ### Than convert that list to a set and print it

        mylargelist = []    #empty list
        for x in range(0, 100):
            mylargelist.append(x)

        print(mylargelist)

        # Now tp convert this large list into a set
        mylargeset = set(mylargelist)
        print(mylargeset)

        genreset = set(tinstruments)
        genreset.add(tgenres)
        genreset.add(tinstcategories)
        print(genreset)



        ### Creating a new dictionary from k/v tuples
        # This one will be with an instrument and the number of strings the instrument has
        instrumentkey = ('bass', 'cello', 'mandolin', 'piano')
        instrumentvalue = (5, 4, 8, 88)
        instrumentdict = dict(zip(instrumentkey, instrumentvalue))
        # Print from the discionary that the bass has 5 strings.
        print(instrumentdict['bass'])


