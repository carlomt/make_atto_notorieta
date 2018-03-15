# -*- coding: utf-8 -*-
#!/usr/bin/python
from __future__ import print_function
import argparse
import bibtexparser
from bibtexparser.bparser import BibTexParser
# from bibtexparser.customization import homogenize_latex_encoding
from bibtexparser.customization import convert_to_unicode
#from bibtexparser.customization import *


# Let's define a function to customize our entries.
# It takes a record and return this record.
def customizations(record):
    """Use some functions delivered by the library

    :param record: a record
    :returns: -- customized record
    """
    record = type(record)
    record = author(record)
    # record = editor(record)
    record = journal(record)
    # record = keyword(record)
    # record = link(record)
    # record = page_double_hyphen(record)
    record = doi(record)
    return record

def simplify(inputfile, limitn=None, verbose=False):
    with open(inputfile,'r') as file:
        bibtex_str = file.read()
        parser = BibTexParser()
        # parser.customization = homogenize_latex_encoding
        parser.customization = convert_to_unicode
        # parser.ignore_nonstandard_types = True
        # parser.homogenise_fields = True
        # parser.common_strings = False
        # parser.encoding = 'utf8'
        # parser.customization = customizations
        bib_database = bibtexparser.loads(bibtex_str, parser=parser)
        for entry in bib_database.entries:
            print("@",str(entry['ENTRYTYPE']),"{",str(entry['unique-id']).strip().translate(None,"{}")+",")
            print("\t author = {",str(entry['author']).strip().split('and')[0]+" and others},")
            print("\t title = {",str(entry['title']).strip(),"},")
            if 'doi' in entry:
                print("\t doi = {",str(entry['doi']).strip(),"},")
            if 'month' in entry:
                print("\t month = {",str(entry['month']).strip(),"},")
            print("\t year = {",str(entry['year']).strip(),"},")
            if 'volume' in entry:
                print("\t volume = {",str(entry['volume']).strip(),"},")
            if 'journal' in entry:
                print("\t journal = {",str(entry['journal']).strip(),"},")
            if 'number' in entry:
                print("\t number = {",str(entry['number']).strip(),"},")
            if 'booktitle' in entry:
                print("\t booktitle = {",str(entry['booktitle']).strip(),"},")                                
            print("}\n")
        # with open('out.bib', 'w') as out_file:
        #     bibtexparser.dump(bib_database, out_file)
            

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                        action="store_true")
    parser.add_argument("-n", "--justn", help="print only the first n papers", type=int)
    parser.add_argument("inputfile", help="input file name (a bib file)")
    args = parser.parse_args()
    
    simplify(args.inputfile, args.justn, args.verbose)

