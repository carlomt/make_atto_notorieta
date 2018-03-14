# -*- coding: utf-8 -*-
#!/usr/bin/python
from __future__ import print_function
import argparse

class paper:

    
    def __init__(self, text):
        self.key     = None        
        self.title   = None
        self.journal = None
        self.year    = None
        self.pages   = None
        self.author  = None
        self.volume  = None
        self.doi     = None
        
        infos = text.split(',')
        self.key = infos[0]        
        for info in infos:
            infs = info.split('=')    
            if "title" in infs[0].lower():
                self.title = self.cleanstring(infs[1])
            if "author" in infs[0].lower():
                tmpauthor = self.cleanstring(infs[1])
                tmpauthor.split('. ')
                if len(tmpauthor)>1:
                    self.author = tmpauthor[0]+". and others"
                else:
                    self.author = tmpauthor
            if len(infs)>1 and "journal" in infs[0].lower():
                self.journal = self.cleanstring(infs[1])
            if len(infs)>1 and "doi" in infs[0].lower():
                self.doi = self.cleanstring(infs[1])                
            if len(infs)>1 and "year" in infs[0].lower():
                self.year = self.cleanstring(infs[1])
            if len(infs)>1 and "volume" in infs[0].lower():
                self.volume = self.cleanstring(infs[1])                                                
            if len(infs)>1 and "pages" in infs[0].lower():
                self.pages = self.cleanstring(infs[1])
                
    def cleanstring(self, instring):
        res = instring.translate(None, '"{}\n\t')
        if res[0]==' ': res=res[1:]
        if res[-1]==' ': res=res[:-1]
        if res[-1]=='.': res=res[:-1]
        return res
    

    def __str__(self):
        message = self.key+",\n"
        for attr, value in self.__dict__.iteritems():
            if value is not None:
                message += "\t"+attr+" = {"+str(value)+"},\n"
        message += "}\n"
        return(message)

    

def simplify(inputfile, verbose=False):
    with open(inputfile,'r') as file:
        inputs = file.read().split('@')
        articles = [a for a in inputs if a[0]!='%']
        for article in articles:
            thisPaper = paper(article)
            print(thisPaper)            

        
if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                        action="store_true")
    parser.add_argument("inputfile", help="input file name (a bib file)")
    args = parser.parse_args()
    
    simplify(args.inputfile, args.verbose)
