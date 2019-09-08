import sys
import yaml



def main():


    with open('troy.yaml', 'r') as f:
        docs = yaml.load_all(f, yaml.FullLoader)
        #docs = yaml.SafeLoader(f)

        for doc in docs:
            for k,v in doc.items():
                print(k, "->", v)
            print("\n")



if __name__ == '__main__':
    main()


