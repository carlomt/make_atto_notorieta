# -*- coding: utf-8 -*-
#!/usr/bin/python
from __future__ import print_function
import argparse

class paper:

    
    def __init__(self, text):
        self.title   = None
        self.journal = None
        self.year    = None
        self.pages   = None
        self.pagerangeisok = 0
        infos = text.split(',')
        for info in infos:
            infs = info.split('=')    
            if "title" in infs[0].lower():
                self.title = self.clean(infs[1])
            if "journal" in infs[0].lower():
                self.journal = self.clean(infs[1])
            if "year" in infs[0].lower():
                self.year = self.clean(infs[1])                                
            if "pages" in infs[0].lower():
                self.pages = self.clean(infs[1])
                
    def startpage(self):
        if self.pages is None or '-' not in self.pages:
            return "TODO"
        self.pagerangeisok = 1
        return self.pages.split('-')[0]

    def endpage(self):
        if self.pages is None or '-' not in self.pages:
            return "TODO"
        splitted1 = self.pages.split('--')
        if splitted1:
            if len(splitted1)>1: return splitted1[1]
        return self.pages.split('-')[1]

    def npage(self):
        try:            
            return str(int(self.endpage())-int(self.startpage()))
        except:
            return "TODO"

    def clean(self, instring):
        res = instring.translate(None, '"{}\n\t')
        if res[0]==' ': res=res[1:]
        if res[-1]==' ': res=res[:-1]
        if res[-1]=='.': res=res[:-1]
        return res
    

    def __str__(self):
        message = ""
        for attr, value in self.__dict__.iteritems():
            message += attr+":   \t"            
            if value is not None:
                message += str(value)+"\n"
            else:
                message += "None\n"                
        return(message)

    

def make_atto_notorieta(inputfile, verbose=False):
    with open(inputfile,'r') as file:
        inputs = file.read().split('@')
        articles = [a for a in inputs if a[0]!='%']
        for article in articles:
            thisPaper = paper(article)
            if verbose: print(article)            

            if verbose: print(thisPaper)
            message='la copia della pubblicazione dal titolo: "'+thisPaper.title+'"'
            if thisPaper.journal is not None:
                message+=' edita da "'+thisPaper.journal+'"'
            if thisPaper.year is not None:
                message+=' nel '+thisPaper.year
            message+=' riprodotta per estratto'
            # if thisPaper.pagerangeisok :
            message +=' da pag. '+thisPaper.startpage()+' a pag. '+thisPaper.endpage()+ ' e quindi composta di '+thisPaper.npage()+ ' fogli'
            message += ' è conforme all’originale \n'
            print(message)

        
                
                
        
    #     for line in file:
    #         if line[0]=='%': continue
    #         if line[0]=='@':
    #             paperid = line.split('{')[1][:-2]
    #             if verbose: print(paperid)
    #             for paperline in file:
    #                 paperlines = paperline.split('=')[:-2]
    #                 if verbose: print(paperlines)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                        action="store_true")
    parser.add_argument("inputfile", help="input file name (a bib file)")
    args = parser.parse_args()
    
    make_atto_notorieta(args.inputfile, args.verbose)
