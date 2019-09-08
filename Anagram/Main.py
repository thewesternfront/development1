import SortClass
import cProfile


def main():
    print("Annagram Algorithm Test")
    sc = SortClass

    # for soem reason I ahve to pass the Object Type in the parentheses
    # for this call to work ... the method in the class has a "self"
    # in the parentheses, find out why ...
    sc.SortItems.doSorting(SortClass)
    sc.SortItems.timingIt(SortClass)
    sc.SortItems.hashingThings(SortClass)

if __name__ == "__main__":
    cProfile.run('main()')

