import sys
import yaml





with open('troy.yaml', 'r') as f:
    docs = yaml.load_all(f)

    for doc in docs:
        for k,v in doc.items():
            print(k, "->", v)
        print("n")







