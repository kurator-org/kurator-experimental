# kurator-experimental
This repo is for cleaning bib records. This specific experiment is to retrive missing titles in the bib records. 

### Description and Prerequisites
The methodology used inhere is to make queries from Google Scholar. The origianl input data is mczbase_IP_publications_2015Aug28.csv. The main code is retrieve_titles.py, which imports module scholar.py. Place the BeautifulSoup.py is required, serving as a Python library for pulling data out of HTML and XML. All those two files should be placed in the same folder as your Python code..

test.py is used for single bib record while retrieve_titles.py is used for batch processing from a csv file.

To run the code, 

  $ python retrieve_titles.py
  
or 

  $ python test.py
  
### Issues
1. There is a bug in retrieve_titles.py. The error information is shown below:
  
  $ python retrieve_titles.py
  
  Traceback (most recent call last):
    File "retrieve_titles.py", line 55, in <module>
      bibtext_new = csv(querier1)
  TypeError: 'module' object is not callable

2. Although missing titles can be retrived, how to verify them?
3. So far only configure the prameter to output the first (most related) result. We can output more results. But for some records, Google Scholar alone might be enough. Below is the list of other potential candidates (for manual search), that might be added in the next step.
  - crossRef
  - [worldCat discovery](https://uiuclib.on.worldcat.org/discovery)
  - web of science: 
  - [national museum of natural history] (http://si-pwebsrch02.si.edu/search?q=&btnG.x=18&btnG.y=7&site=nmnh&client=nmnh_mainsite&proxystylesheet=nmnh_mainsite&output=xml_no_dtd)
  - [American museum of natural history] (http://www.amnh.org/our-research/research-library/library-catalog/)

