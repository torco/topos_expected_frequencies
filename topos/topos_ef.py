import pandas as pd
import pathlib
import os



def get_keywords(text, language, num=10):
    
    print('topos -- starting text of length',len(text))
    text = text.replace(':',',').replace(';',',').replace('!',','.replace('?',','))
    text = text.replace(',',' ').replace('.',' ').replace('  ',' ')
    
    if type(text)!=str:
        raise TypeError('first parameter ought be a long string for keywords to be extracted')
    if type(language)!=str:
        raise TypeError('second parameter ought be a string, representing one of the supported languages')
    if type(num)!=int:
        raise TypeError('third parameter, if used, must be int.')
        
    dir_path = str(pathlib.Path(__file__).parent.resolve())
    if language=='ara':
        size_parameter=3
        freqlist=pd.read_csv(dir_path+'/corpus_arabic.txt', sep=' ', on_bad_lines='skip', nrows=25000)
    elif language == 'zh':
        size_parameter=1
        freqlist=pd.read_csv(dir_path+'/corpus_chinese.txt', sep=' ', on_bad_lines='skip', nrows=25000)
    elif language == 'en':
        size_parameter=3
        freqlist=pd.read_csv(dir_path+'/corpus_english.txt', sep=' ', on_bad_lines='skip', nrows=25000)
    elif language == 'es':
        size_parameter=3
        freqlist=pd.read_csv(dir_path+'/corpus_español.txt', sep='|', on_bad_lines='skip', nrows=35000)        
    elif language == 'fr':
        size_parameter3
        freqlist=pd.read_csv(dir_path+'/corpus_francais.txt', sep=' ', on_bad_lines='skip', nrows=25000)        
    elif language == 'de':
        size_parameter=3
        freqlist=pd.read_csv(dir_path+'/corpus_german.txt', sep='\t', on_bad_lines='skip', nrows=25000).drop(columns=['x','x2'])
    elif language == 'it':
        size_parameter=3
        freqlist=pd.read_csv(dir_path+'/corpus_italiano.txt', sep=' ', on_bad_lines='skip', nrows=25000)
    elif language == 'ja':
        size_parameter=1
        freqlist=pd.read_csv(dir_path+'/corpus_nihongo.txt', sep=' ', on_bad_lines='skip', nrows=25000)
    elif language == 'ru':
        size_parameter=3
        freqlist=pd.read_csv(dir_path+'/corpus_ruso.txt', sep=' ', on_bad_lines='skip', nrows=55000)
    else:
        raise Exception("language not supported: the second parameter should be one of ara, zh, en, es, fr, de, it, ja, ru.")
        
    words=[]
    for word in text.split(' '):
      if word not in words and len(word) > size_parameter:
        if word in freqlist['form'].values : words.append(word)
    words = pd.DataFrame(data=words)
    
    if len(words)<1: raise Exception("could not obtain words to examine: check that the input is valid")
    
    total_in_input = len(text.split(' '))
    for index, word in words.iterrows():
      count=text.count(word[0])
      words.at[index,'count']=count
    print(total_in_input,' words in text')
      
    crea=freqlist
    for index, word in words.iterrows():
      ppm=((word['count'])/total_in_input)*1000000
      wo = word[0]
      words.at[index,'freq']=ppm
      words.at[index,'expected_freq']=0
      crealine = crea[crea['form']==wo]
      if crealine.empty == False:
        ppmrae = crea[crea['form']==wo]
        numb = ppmrae.iat[0,1]
        words.at[index,'expected_freq']=numb
        words.at[index,'ratio']=ppm/numb
    words=words.sort_values(by='ratio', ascending=False)[0:num]
    return words

def hi():
    print('hi hi')
    
#b = get_keywords('que tenemos las habilidades. no sólo las que nos encontramos buscando sino también las que podemos ir a ver.', 'es', 10)
#a = get_keywords('notice the xxxx,theres around you as they appear in your consciousnes. direct your attention to whatever sensations you can feel.', 'en')
