from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.title_start = False
        self.title_end = False
        self.title_data = []
    def handle_starttag(self, tag, attrs):
        print "Encountered a start tag:", tag
        if tag == "title":
            #print "Encountered a start tag:", tag
            self.title_start = True
            self.title_end = False
    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag
        if tag == "title":
            self.title_end = True
            self.title_start = False
    def handle_data(self, data):
        if self.title_start == True and self.title_end == False:
            print "Encountered some data  :", data
            self.title_data.append(data)
        else:
            print "Encountered some data  :", data
    def print_title_data(self):
        print self.title_data
#    def feed(self, data):
#        print data
# instantiate the parser and fed it some HTML
parser = MyHTMLParser()

parser.feed('<html><head><title>Test, Hello, Bye</title></head>'
            '<body><h1>Parse me!</h1></body><title>Jay Shri Ram</title></html>')
parser.print_title_data()

'''
D:\F DATA\python_class\generic>python htmlparser.py
Encountered a start tag: html
Encountered a start tag: head
Encountered a start tag: title
Encountered some data  : Test, Hello, Bye
Encountered an end tag : title
Encountered an end tag : head
Encountered a start tag: body
Encountered a start tag: h1
Encountered some data  : Parse me!
Encountered an end tag : h1
Encountered an end tag : body
Encountered a start tag: title
Encountered some data  : Jay Shri Ram
Encountered an end tag : title
Encountered an end tag : html
['Test, Hello, Bye', 'Jay Shri Ram']
'''