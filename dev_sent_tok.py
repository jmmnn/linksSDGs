import os
import glob
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize


#configurations
source = './test/'
destination = './test_out/'
file_filter = '*.txt'

#This obtains the list of files to process
os.chdir(source)                    #move to source dir
file_list = glob.glob(file_filter)  
os.chdir("..")                      #return to starting dir

# place here your function to execute on each filea 
def sent_extract (filename):
    f = open(source+filename , 'rU')
    raw = f.read().decode('utf8')
    all_sent = sent_tokenize(raw)
    print all_sent

#This is where teh magic happens
def iterdir(function):
    for i in range(len(file_list)):
        function(file_list[i]) #
        print ('done ' + file_list[i])
    print(' ......All done ...')
    
    
#run-it calling the function you want to run
iterdir(sent_extract)  # running the function of choice