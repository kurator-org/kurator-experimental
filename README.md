# kurator-experimental


### Description
This repository has two sub-directories. 

1. The Kurator-bib is for cleaning bib records. This specific experiment is to retrive missing titles in the bib records. The methodology used inhere is to make queries from Google Scholar. The origianl input data is mczbase_IP_publications_2015Aug28.csv. The main code is retrieve_titles.py, which imports module scholar.py. Place the BeautifulSoup.py is required, serving as a Python library for pulling data out of HTML and XML. All those two files should be placed in the same folder as your Python code. test.py is used for single bib record while retrieve_titles.py is used for batch processing from a csv file.

  To run the code, 
  
a). remove the carriage returns in original csv file:
  
    $ python remove_carriage_returns.py mczbase_IP_publications_2015Aug28.csv mczbase_IP_publications_2015Aug28_remove_carriage_returns.csv 

b). run the main function to retrive missing titles from Google Scholar:

    $ python retrieve_titles.py
  
  
  ##### Issues
  The latest update has fixed two erros and now has retrieved dataset store in output/ directory. The current status is 62 out of 581 bib records have been found a match through Google Scholar. The next steps are: 

  (1). Although missing titles can be retrived, how to verify them?

  (2). So far only configure the prameter to output the first (most related) result. We can output more results. But for some records,   Google Scholar alone might be enough. Below is the list of other potential candidates (for manual search), that might be added in the next step.
  - crossRef
  - [worldCat discovery](https://uiuclib.on.worldcat.org/discovery)
  - web of science: 
  - [national museum of natural history] (http://si-pwebsrch02.si.edu/search?q=&btnG.x=18&btnG.y=7&site=nmnh&client=nmnh_mainsite&proxystylesheet=nmnh_mainsite&output=xml_no_dtd)
  - [American museum of natural history] (http://www.amnh.org/our-research/research-library/library-catalog/)

2. The second repo is using Python to develop a frontend interface for Kurator workflow. The web app is based on Flask framework and it is still under development.
