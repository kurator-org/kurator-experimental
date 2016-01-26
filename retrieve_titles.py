from scholar import * 
import os
import csv
import sys

fr = open('mczbase_IP_publications_2015Aug28.csv','rb')
reader = csv.reader(fr)
fw = open('new.csv', 'w')
# write into a new file
writer = csv.writer(fw,lineterminator='\n')

#count total number of rows
row_count = 0

for i, row in enumerate(reader):    
    row_count += 1
    if i == 0:
        new_attr = ['title','url','year','num_citations','num_versions','cluster_id','url_pdf','url_citations','url_versions','url_citation','excerpt']
        row.extend(new_attr)
        writer.writerow(row)
    else:
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
        query1.set_timeframe(bib_year,None)
        settings1 = ScholarSettings()
#        settings1.set_citation_format(ScholarSettings.CITFORM_BIBTEX)
        querier1.apply_settings(settings1)
        querier1.send_query(query1)
        print i
        bibtext_new = csv(querier1)
        print type(bibtext_new)
        if bibtext_new is not None and "|" in bibtext_new:
                bibtext_new_attr = bibtext_new.split('|')
                for item in bibtext_new_attr:
                    # print item
                    row.append(item)
        else: 
            print "No result!"
        writer.writerow(row)
        del bibtext_orig, querier1, query1, bibtext_new

#finally:
fr.close()
fw.close()
print 'total_rows = %d' % row_count 

if __name__ == "__main__":
    sys.exit(main())
