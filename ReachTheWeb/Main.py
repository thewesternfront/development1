
import urllib.request
import urllib.parse
import sys
my_url = "http://www.brainjar.com/java/host/test.html"


def reachTheWeb():
    print("Accessing ...")

    my_url = "http://www.brainjar.com/java/host/test.html"

    try:
        with urllib.request.urlopen(my_url)as doc:
            html = doc.read()
    except:
        print("could not open %s" % doc, file = sys.err)

    print("The contents of the web page are \n")
    print(html)


def parseURL(url_to_parse):
    print("Parsing a URL")
    my_parsed_url = urllib.parse.urlparse(my_url)
    print(my_parsed_url)


def main():
    print("reaching the web in Python")
    reachTheWeb()
    parseURL(my_url)


if __name__ == '__main__':
    main()
