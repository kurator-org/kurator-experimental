# -*- coding: utf-8 -*-     
# Defining Python Source Code Encodings https://www.python.org/dev/peps/pep-0263/
import scholar
import timestamp
import os
import csv
import sys

print 'Python version: ' + str(sys.version_info[0])

def add_title_using_gscholar(
    input_data_file_name,
    output_data_file_name,
    input_field_delimiter=',',
    output_field_delimiter=',',
    ):

    found_match_count = 0
    nofound_match_count = 0
    
    # create csv reader for input records
    timestamp.timestamp("Reading input records from '{0}'.".format(input_data_file_name))
    fr = open(input_data_file_name,'rb')
    input_data = csv.DictReader(fr, delimiter = input_field_delimiter)
    
    # fieldnames/keys of original input data (dictionary)
    original_data_fieldnames = input_data.fieldnames
    
    # find corresponding column position for specified header
    author_pos = fuzzymatch(original_data_fieldnames,'author')
    year_pos = fuzzymatch(original_data_fieldnames,'year')
    title_pos = fuzzymatch(original_data_fieldnames,'title')
    journal_pos = fuzzymatch(original_data_fieldnames,'journal')
    publisher_pos = fuzzymatch(original_data_fieldnames,'publisher')
    volume_pos = fuzzymatch(original_data_fieldnames,'volume')
    issue_pos = fuzzymatch(original_data_fieldnames,'issue')
    page_pos = fuzzymatch(original_data_fieldnames,'page')
    
    #count total data records
    record_num = 0
    
    for original_record in input_data:
        record_num += 1
        print
        timestamp.timestamp("Reading input record '{0:05d}'.".format(record_num))
        # exact values of fields to be validated
        original_record_title = original_record[title_pos.values()[0]]
        original_record_author = original_record[author_pos.values()[0]]
        original_record_year = original_record[year_pos.values()[0]]
        original_record_journal = original_record[journal_pos.values()[0]]
    
        if original_record_author == "[no agent data]":
            original_record_author = None
        if original_record_year == "0" or original_record_year == "":
            original_record_year = None
        if original_record_title == "no article title available":
            original_record_title = None
        if original_record_journal == "":
            original_record_journal = None
        
        output_record = original_record
        gscholar_match_result = None
        
        # try match search of the combination of author, publicaton year, title (if existing), and journal name.
        timestamp.timestamp("Trying Google Scholar match search for original record: '{0}'.".format(original_record)) 
        querier1 = scholar.ScholarQuerier()
        query1 = scholar.SearchScholarQuery()
        query1.set_num_page_results(1)
        query1.set_author(original_record_author)
        query1.set_pub(original_record_journal)
        query1.set_scope(original_record_title)
        if original_record_year is not None:          
            # extend the publisher year to an interval [original_record_year-10 original_record_year+10]
            query1.set_timeframe(str(int(original_record_year)-10),str(int(original_record_year)+10))
        else:
            query1.set_timeframe(None,None)
        settings1 = scholar.ScholarSettings()
        settings1.set_citation_format(scholar.ScholarSettings.CITFORM_BIBTEX)
        querier1.apply_settings(settings1)
        querier1.send_query(query1)        
        gscholar_record = scholar.citation_export(querier1) 
        if len(gscholar_record) < 1:
            timestamp.timestamp('Google Scholar match FAILED!')
            nofound_match_count += 1
        else:
            timestamp.timestamp('Google Scholar match was SUCESSFUL!')
            gscholar_match_result = True
            found_match_count += 1
            gscholar_record_str = gscholar_record[0]
            if gscholar_record_str.find('@') > -1:
                at_type = gscholar_record_str.find('@')
                sp_type = gscholar_record_str.find('{',at_type)
                new_type = gscholar_record_str[at_type+1 : sp_type]
                output_record['type'] = new_type
            if gscholar_record_str.find('title={') > -1:      
                at_title = gscholar_record_str.find('title={')
                sp_title = gscholar_record_str.find('}',at_title)
                new_title = gscholar_record_str[at_title+7 : sp_title]
                output_record['title'] = new_title 
            if gscholar_record_str.find('author={') > -1:
                at_author = gscholar_record_str.find('author={')
                sp_author = gscholar_record_str.find('}',at_author)
                new_author = gscholar_record_str[at_author+8 : sp_author]
                output_record['author'] = new_author
            if gscholar_record_str.find('journal={') > -1:
                at_journal = gscholar_record_str.find('journal={')
                sp_journal = gscholar_record_str.find('}',at_journal)
                new_journal = gscholar_record_str[at_journal+9 : sp_journal]
                output_record['journal'] = new_journal      
            if gscholar_record_str.find('volume={') > -1:
                at_volume = gscholar_record_str.find('volume={')
                sp_volume = gscholar_record_str.find('}',at_volume)
                new_volume = gscholar_record_str[at_volume+8 : sp_volume]
                output_record['volume'] = new_volume 
            if gscholar_record_str.find('pages={') > -1:
                at_pages = gscholar_record_str.find('pages={')
                sp_pages = gscholar_record_str.find('}',at_pages)
                new_pages = gscholar_record_str[at_pages+7 : sp_pages]
                output_record['pages'] = new_pages 
            if gscholar_record_str.find('year={') > -1:
                at_year = gscholar_record_str.find('year={')
                sp_year = gscholar_record_str.find('}',at_year)
                new_year = gscholar_record_str[at_year+6 : sp_year]
                output_record['year'] = new_year
            if gscholar_record_str.find('publisher={') > -1:
                at_publisher = gscholar_record_str.find('publisher={')
                sp_publisher = gscholar_record_str.find('}',at_publisher)
                new_publisher = gscholar_record_str[at_publisher+11 : sp_publisher]
                output_record['publisher'] = new_publisher               
    
        # open file for storing output data if not already open
        if 'output_data' not in locals():
            extra_fieldnames = ['type','title','author','journal','volume','pages','year','publisher']
            output_data_fieldnames = input_data.fieldnames + extra_fieldnames
            fw = open(output_data_file_name,'w')
            output_data = csv.DictWriter(fw,output_data_fieldnames,
                                        delimiter = output_field_delimiter)
            output_data.writeheader()
        output_data.writerow(output_record)
        
    print
    timestamp.timestamp("Summary: {0} matches found and {1} matches not found to '{2}'.".format(found_match_count, nofound_match_count, output_data_file_name))

    fr.close()
    fw.close()                                        
            
def fuzzymatch(lst, label_str):
    pos = 0
    for key in lst:
        pos += 1 
        mat_dict = {}
        if key.lower().find(label_str) > -1:
            header_name = key
            mat_dict[label_str] = header_name
            break
        else:            
            mat_dict[label_str] = None
    return mat_dict           
        
    


if __name__ == '__main__':
    '''Demo of add_title_using_gscholar script'''
    add_title_using_gscholar(
        input_data_file_name = 'mczbase_IP_publications_2015Aug28_remove_carriage_returns.csv',
        output_data_file_name = 'demo_output.csv'
    )
