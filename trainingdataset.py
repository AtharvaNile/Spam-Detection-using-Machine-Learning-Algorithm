import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords          #is,his,as etc.
from nltk.tokenize import wordpunct_tokenize   #remove =,\n etc.

from os import listdir    #read all files
from os.path import isfile, join


nltk.data.path = ['C:\ nltk_data']

stopwords = set(stopwords.words('english'))

spam_path = 'C:/Users/Micky/Desktop/sdlpro/data/spam/'
ham_path = 'C:Users/Micky/Desktop/sdlpro/data/ham/'

def get_words(message):
    
    all_words = set(wordpunct_tokenize(message.replace('=\\n', '').lower()))
    
    msg_words = [word for word in all_words if word not in stopwords and len(word) > 2]
    
    return msg_words
    
def get_mail_from_file(file_name):
    
    message = ''
    
    with open(file_name, 'r') as mail_file:
        
        for line in mail_file:
            
            if line == '\n':      #contents of mail start after newline
              
                for line in mail_file:
                    message += line             #string outta remaining lines
                    
    return message
    
    
    
def make_training_set(path):
# dictionary : <term>:<occur>    
    training_set = {}

    mails_in_dir = [mail_file for mail_file in listdir(path) if isfile(join(path, mail_file))]
    
    cmds_count = 0           #count of cmds in a folder
    total_file_count = len(mails_in_dir)
    
    for mail_name in mails_in_dir:
        
        if mail_name == 'cmds':
            cmds_count += 1
            continue
       
        message = get_mail_from_file(path + mail_name)
        
        terms = get_words(message)            #words
        
        #add entries to training dataset
        for term in terms:
            if term in training_set:
                training_set[term] = training_set[term] + 1
            else:
                training_set[term] = 1
    
    total_file_count -= cmds_count
    # calculate the occurrence for each term
    for term in training_set.keys():
        training_set[term] = float(training_set[term]) / total_file_count
                            
    return training_set

print ''    
print 'Loading training sets...',
spam_training_set = make_training_set(spam_path)
ham_training_set = make_training_set(ham_path)
print 'done.'
print ''
