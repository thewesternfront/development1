import GraphClass
import DataStructures
import FileOps
import ReachTheWeb


def main():
    print("Instantiating all of my classes")
    gc = GraphClass
    ds = DataStructures
    fo = FileOps
    theweb = ReachTheWeb

    #gc.Graphing.setupGraph(GraphClass)
    #ds.DataStructures.setupFourDs(DataStructures)
    fo.FileOps.writeListToFile(FileOps)


if __name__ == "__main__":
    main()
