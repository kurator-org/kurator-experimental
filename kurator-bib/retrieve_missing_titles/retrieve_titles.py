# -*- coding: utf-8 -*-     
# Defining Python Source Code Encodings https://www.python.org/dev/peps/pep-0263/
from scholar import *
import os
import csv
import sys
import chardet
'''
# coding=latin-1    # not working
$pip install chardet
Note1: Google scholar is unstable (sometimes down), returning no results at all ("--csv" works but "--citation bt" not working). 
Note2: It's better to use VPN if working at home.
'''
print 'Python version: ' + str(sys.version_info[0])
fr = open('mczbase_IP_publications_2015Aug28.csv','rb')
# import codecs
# f=codecs.open ('somefile.txt', 'rt', encoding='utf-8').read()
reader = csv.reader(fr)
fw = open('new.csv', 'w')
# tp = chardet.detect(reader)
# charenc = tp['encoding']
# print charenc
# write into a new file
writer = csv.writer(fw,lineterminator='\n')

#count total number of rows
row_count = 0
nu = 0
for i, row in enumerate(reader):        
    if i == 0:
        new_attr = ['type','title','author','journal','volume','pages','year','publisher']
        row.extend(new_attr)
        writer.writerow(row)
    else:
        row_count += 1
        bibtext_orig = row
        bib_ID = bibtext_orig[0]
        bib_author = bibtext_orig[1]
        bib_year = bibtext_orig[2]
        bib_title = bibtext_orig[3]
        bib_journal = bibtext_orig[4]
        bib_journal_abb = bibtext_orig[5]
        bib_volume = bibtext_orig[6]
        bib_issue = bibtext_orig[7]
        bib_bgn_pg = bibtext_orig[8]
        bib_end_pg = bibtext_orig[9]
        bib_publisher = bibtext_orig[10]
        if bib_author == "[no agent data]":
            bib_author = None
        if bib_year == "0" or bib_year == "":
            bib_year = None
        if bib_title == "no article title available":
            bib_title = None
        if bib_journal == "":
            bib_journal = None
#        print bibtext_orig, bib_ID, bib_author, bib_year, bib_title, bib_journal, bib_journal_abb, bib_volume, bib_issue, bib_bgn_pg, bib_end_pg, bib_publisher
        querier1 = ScholarQuerier()
        query1 = SearchScholarQuery()
        query1.set_num_page_results(1)
        query1.set_author(bib_author)
        query1.set_pub(bib_journal)
        query1.set_scope(bib_title)
        if bib_year is not None:
            # extend the publisher year to an interval [bib_year-10 bib_year+10]
            query1.set_timeframe(str(int(bib_year)-10),str(int(bib_year)+10))
        else:
            query1.set_timeframe(None,None)
        settings1 = ScholarSettings()
        settings1.set_citation_format(ScholarSettings.CITFORM_BIBTEX)
        querier1.apply_settings(settings1)
        querier1.send_query(query1)
        print 'Row ' + str(i) + ':'
        # citation_export(querier1)
        bibtext_new = citation_export(querier1)    
        print bibtext_new  # return a list containing one string
        # print len(bibtext_new)  # return 1 = length of list 
        # print len(bibtext_new[0])  # return length of string
        if len(bibtext_new) < 1:
            print 'no search result'
            row.append("no result")
            writer.writerow(row)
        else: 
            nu = nu + 1
            bibtext_new_str = bibtext_new[0]
            # print bibtext_new_str # return the string
            if bibtext_new_str.find('@') == -1:
                row.append('')
            else:
                at_type = bibtext_new_str.find('@')
                # print at_type
                sp_type = bibtext_new_str.find('{',at_type)
                # print sp_type
                new_type = bibtext_new_str[at_type+1 : sp_type]
                print new_type
                row.append(new_type)
            if bibtext_new_str.find('title={') == -1:
                row.append('')
            else:       
                at_title = bibtext_new_str.find('title={')
                # print at_title
                # print bibtext_new_str[int(at_title)]
                sp_title = bibtext_new_str.find('}',at_title)
                # print sp_title
                # print bibtext_new_str[int(sp_title)]
                new_title = bibtext_new_str[at_title+7 : sp_title]
                print new_title
                row.append(new_title) 
            if bibtext_new_str.find('author={') == -1:
                row.append('')
            else:
                at_author = bibtext_new_str.find('author={')
                # print at_author
                # print bibtext_new_str[int(at_author)]
                sp_author = bibtext_new_str.find('}',at_author)
                # print sp_author
                # print bibtext_new_str[int(sp_author)]
                new_author = bibtext_new_str[at_author+8 : sp_author]
                print new_author
                row.append(new_author) 
            if bibtext_new_str.find('journal={') == -1:
                row.append('')
            else:
                at_journal = bibtext_new_str.find('journal={')
                # print at_journal
                # print bibtext_new_str[int(at_journal)]
                sp_journal = bibtext_new_str.find('}',at_journal)
                # print sp_journal
                # print bibtext_new_str[int(sp_journal)]
                new_journal = bibtext_new_str[at_journal+9 : sp_journal]
                print new_journal
                row.append(new_journal)      
            if bibtext_new_str.find('volume={') == -1:
                row.append('')
            else:
                at_volume = bibtext_new_str.find('volume={')
                # print at_volume
                # print bibtext_new_str[int(at_volume)]
                sp_volume = bibtext_new_str.find('}',at_volume)
                # print sp_volume
                # print bibtext_new_str[int(sp_volume)]
                new_volume = bibtext_new_str[at_volume+8 : sp_volume]
                print new_volume
                row.append(new_volume) 
            if bibtext_new_str.find('pages={') == -1:
                row.append('')
            else:
                at_pages = bibtext_new_str.find('pages={')
                # print at_pages
                # print bibtext_new_str[int(at_pages)]
                sp_pages = bibtext_new_str.find('}',at_pages)
                # print sp_pages
                # print bibtext_new_str[int(sp_pages)]
                new_pages = bibtext_new_str[at_pages+7 : sp_pages]
                print new_pages
                row.append(new_pages) 
            if bibtext_new_str.find('year={') == -1:
                row.append('')
            else:
                at_year = bibtext_new_str.find('year={')
                # print at_year
                # print bibtext_new_str[int(at_year)]
                sp_year = bibtext_new_str.find('}',at_year)
                # print sp_year
                # print bibtext_new_str[int(sp_year)]
                new_year = bibtext_new_str[at_year+6 : sp_year]
                print new_year
                row.append(new_year) 
            if bibtext_new_str.find('publisher={') == -1:
                row.append('')
            else:
                at_publisher = bibtext_new_str.find('publisher={')
                # print at_publisher
                # print bibtext_new_str[int(at_publisher)]
                sp_publisher = bibtext_new_str.find('}',at_publisher)
                # print sp_publisher
                # print bibtext_new_str[int(sp_publisher)]
                new_publisher = bibtext_new_str[at_publisher+11 : sp_publisher]
                print new_publisher
                row.append(new_publisher) 
            # print row
            writer.writerow(row)        
print 'Match found: ' + str(nu)
#finally:
fr.close()
fw.close()
print 'total_rows = %d' % row_count 

if __name__ == "__main__":
    sys.exit(main())