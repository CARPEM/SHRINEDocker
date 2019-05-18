from html.parser import HTMLParser

# create a subclass and override the handler methods
class HTMLParser4OsirisValue(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.data=[]
        self.open=False
        self.body=False
        self.getCode=False
        self.getLabel=False
        #self.convert_charrefs=True
        self.current={}
        self.code=""
        self.label=""

    def handle_starttag(self, tag, attrs):
        if tag == 'a' :
            for attr in attrs:
                if attr[0]=='href' and 'conceptualdomain' in attr[1] :
                    # print(attr)
                    self.open=True
                    # print(self.open)

        if tag == 'tbody' :
            if self.open :
                self.body=True

        if self.open and self.body :
            # print(tag)
            if tag == 'tr':
                self.getCode=True
                # print(self.getCode)

    def handle_data(self, data):
        if self.getLabel :
            if data != '\n':
                self.current["Label"]= data.replace(',',' ')
                #print('data ' + data)
                self.getLabel=False
        if self.getCode :
            if data != '\n':
                code = data
                if ":" not in code : code = "os:"+code
                self.current["code"]=code
                # print('data ' + data)
                # print(self.current)
                self.getCode=False
                self.getLabel=True
                # print(self.getCode)


    def handle_endtag(self, tag):
      if tag == 'tr' :
        if self.open and self.body:
            self.data.append(self.current.copy())
            # print(self.data)
            self.getCode=False
