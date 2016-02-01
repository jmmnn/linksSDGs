# -*- coding: utf-8 -*-

"""This program takes a list of .txt files and extracts all sentences which mention any SDG, 
    based on the list of keywords below for each SDG."""
import sys
import solr
from random import randint

############# CONFIGURATION #############
#file and folders

search_collection = 'linksdgs'
search_server = 'http://solr-jmmnn-1.c9users.io/solr/' + str(search_collection)

#########################################


s = solr.SolrConnection(search_server)  # Search server details 

#s.add(sentence = phrase, sdg = SDGs , publication = pub_name)

# s.delete_query('*:*')
# s.commit()

response = s.query('*:*')

for hit in response.results:
    #print hit['sentence']
    print hit


a = 'a5cde7g'



# #!/usr/bin/python

# try:
#   fh = open("testfile", "r")
#   fh.write("This is my test file for exception handling!!")
# except IOError:
#   print "Error: can\'t find file or read data"
# else:
#   print "Written content in the file successfully"
#   fh.close()
   
#!/usr/bin/python

# # Define a function here.
# def temp_convert(var):
#     try:
#         print int(letter)

#     except:
#         print "Error : "

# # Call above function here.
# for letter in a:
#     temp_convert(letter)