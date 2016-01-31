from scholar import * 

'''
# example1:
# Retrieve one article written by Einstein on quantum theory:
# scholar.py -c 1 --author "albert einstein" --phrase "quantum theory" --csv
print 'example1: scholar.py -c 1 --author \"albert einstein\" --phrase \"quantum theory\" --csv'
querier1 = ScholarQuerier()
query1 = SearchScholarQuery()
query1.set_num_page_results(1)
query1.set_author("albert einstein")
query1.set_phrase("quantum theory")
# query1.set_timeframe(1970, 1990)
settings1 = ScholarSettings()
# settings1.set_citation_format(ScholarSettings.CITFORM_BIBTEX)
querier1.apply_settings(settings1)
querier1.send_query(query1)
# citation_export(querier1)
fcsv(querier1)    # return result!
# print type(fcsv(querier1))
'''

'''
# example2: 
# retrieve the first record in MCZBase dataset
print 'example2: scholar.py -c 1 --author \"Agassiz, L.\" --after 1839 --pub \"Soc.Sci.Nat. Helvetica Mem.\" --csv'
querier1 = ScholarQuerier()
query1 = SearchScholarQuery()
query1.set_num_page_results(3)
query1.set_author("Agassiz, L.")
#query1.set_phrase("quantum theory")
query1.set_timeframe(1839, None)
query1.set_pub("Soc.Sci.Nat. Helvetica Mem.")
settings1 = ScholarSettings()
# settings1.set_citation_format(ScholarSettings.CITFORM_BIBTEX)
querier1.apply_settings(settings1)
querier1.send_query(query1)
# citation_export(querier1)
fcsv(querier1)
print type(fcsv(querier1))  # print + type, ==> print result twice
bibtext_new = fcsv(querier1)    # assign excerpt value
'''

# example3:
# Retrieve one article written by Einstein on quantum theory:
# scholar.py -c 1 --author "albert einstein" --phrase "quantum theory" --citation bt
print 'example3: scholar.py -c 1 --author \"albert einstein\" --phrase \"quantum theory\" --citation bt'
querier1 = ScholarQuerier()
query1 = SearchScholarQuery()
query1.set_num_page_results(1)
query1.set_author("albert einstein")
query1.set_phrase("quantum theory")
# query1.set_timeframe(1970, 1990)
settings1 = ScholarSettings()
settings1.set_citation_format(ScholarSettings.CITFORM_BIBTEX)
querier1.apply_settings(settings1)
querier1.send_query(query1) # return nothing 
# print querier1.send_query(query1)   # return none
# print type(querier1.send_query(query1))
# citation_export(querier1)   # return result
# type(citation_export(querier1)) # return result
bibtext_new = citation_export(querier1)    # return result
# print bibtext_new  # return a list containing one string
# print len(bibtext_new)  # return 1 = length of list 
# print len(bibtext_new[0])  # return length of string
nu = 0
if len(bibtext_new) < 1:
    row.append("no result")
    writer.writerow(row)
else: 
    nu = nu + 1
    row = list()
    print row
    bibtext_new_str = bibtext_new[0]
    print bibtext_new_str   # return the string
    print len(bibtext_new_str)
    #print bibtext_new_str[0]
    #print bibtext_new_str[1]
    #print bibtext_new_str[5]
    #print bibtext_new_str[25]
    #print bibtext_new_str[26]
    #print bibtext_new_str[29]
    #print bibtext_new_str[-1]
    #print bibtext_new_str[274]
    # find type
    print bibtext_new_str.find('@') is True
    print bibtext_new_str.startswith('@') is True
    # print bibtext_new_str.startswith('@') 
    if bibtext_new_str.find('@') == -1:
        row.append('')
    else:
        at_type = bibtext_new_str.find('@')
        print at_type
        sp_type = bibtext_new_str.find('{',at_type)
        print sp_type
        new_type = bibtext_new_str[at_type+1 : sp_type]
        print new_type
        row.append(new_type)
    if bibtext_new_str.find('title={') == -1:
        row.append('')
    else:
        at_title = bibtext_new_str.find('title={')
        print at_title
        print bibtext_new_str[int(at_title)]
        sp_title = bibtext_new_str.find('}',at_title)
        print sp_title
        print bibtext_new_str[int(sp_title)]
        new_title = bibtext_new_str[at_title+7 : sp_title]
        print new_title
        row.append(new_title) 
    if bibtext_new_str.find('author={') == -1:
        row.append('')
    else:
        at_author = bibtext_new_str.find('author={')
        print at_author
        print bibtext_new_str[int(at_author)]
        sp_author = bibtext_new_str.find('}',at_author)
        print sp_author
        print bibtext_new_str[int(sp_author)]
        new_author = bibtext_new_str[at_author+8 : sp_author]
        print new_author
        row.append(new_author) 
    print row
    '''
    bibtext_new_attrs = bibtext_new_str.split('\n') # split by '\n'
    print bibtext_new_attrs # a list of strings
    print len(bibtext_new_attrs)
    for att in bibtext_new_attrs:
        print att   # print att


    #for attr in bibtext_new_attrs:
    # print attr
    if bibtext_new_str.find('@'):
        at_type = bibtext_new_str.find('@')
        sp_type = bibtext_new_str.find('{',at_type)
        new_type = bibtext_new_str[at_type+1 : sp_type]
    # if len(new_type) > 0:
        row.append(new_type)
    else:
        row.append('')
        if bibtext_new_str.find('title={'):
            at_title = bibtext_new_str.find('title={')
            sp_title = bibtext_new_str.find('}',at_title)
            new_title = bibtext_new_str[at_title+1 : sp_title]
    #if len(new_title) > 0:
            row.append(new_title)
        else:
            row.append('')
            if bibtext_new_str.find('author={'):
                at_author = bibtext_new_str.find('author={')
                sp_author = bibtext_new_str.find('}',at_author)
                new_author = bibtext_new_str[at_author+1 : sp_author]                       
                row.append(new_author)
print "print row:"
print row
'''