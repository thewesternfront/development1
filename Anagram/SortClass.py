import timeit


class SortItems:

    def doSorting(self):

        # set the strings to compare
        a1 = "qpwoeirutyalskdjfhgzmxncbv"
        a2 = "qwertyuioplkjhgfdsazxcvbnm"

        # first check is if they are equal length, if not, no need proceeding
        if len(a1) == len(a2):

            # Sort strign in alphabetical order
            a1res = ''.join(sorted(a1))
            a2res = ''.join(sorted(a2))

            print(a1res)
            print(a2res)

            # check for identical strings
            if a1res == a2res:
                print("The strings are an Annagram")
            else:
                print("The strings are not an Annagram")

        else:
            print("The strings are differing lengths")

    def timingIt(self):
        print(timeit.timeit("x=2+2"))
        print(timeit.timeit("x=sum(range(10))"))

    def hashingThings(self):
        print("Lets Perform A Hash")
        print(hash(42))
        print(hash("Troy West"))
        print("Hash is completed")