from scholar import * 

# example1:
# Retrieve one article written by Einstein on quantum theory:
# scholar.py -c 1 --author "albert einstein" --phrase "quantum theory"
querier1 = ScholarQuerier()
query1 = SearchScholarQuery()
query1.set_num_page_results(3)
query1.set_author("albert einstein")
query1.set_phrase("quantum theory")
query1.set_timeframe(1970, 1990)
settings1 = ScholarSettings()
# settings1.set_citation_format(ScholarSettings.CITFORM_BIBTEX)
querier1.apply_settings(settings1)
querier1.send_query(query1)
# citation_export(querier1)
csv(querier1)
print type(csv(querier1))

# example2: 
# retrieve the first record in MCZBase dataset
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
csv(querier1)
print type(csv(querier1))
