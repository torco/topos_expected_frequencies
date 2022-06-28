ToposFreq is a library that automatically highlights the most topical words in a given large text. it supports English, Spanish, French, Italian, German, Arabic, Chinese, Japanese and Russian. It is a technique for determining term frequency not based on tf-idf, but rather, on tf/cf. 

HOW TO USE

get_keywords(text, language, num)

text(string): the text you want Topos to examine.

language(string): it admits 
'ara'	arabic
'zh'	chinese
'en'	english
'es'	spanish
'fr'  french
'de'  german
'it'  italian
'ja'  japanese
'ru'  russian

num: an int representing how many terms you want topos to output. 

the function will produce output in the form of a pandas dataframe.

The corpuses were obtained mostly from from Sharov(2006):
http://corpus.leeds.ac.uk/frqc/

Spanish was sourced from the CREA corpus put together by the Real Academia Española
https://www.rae.es/banco-de-datos/crea

##############   rationale   ###############

Typically, topic modeling (broadly speaking, answering the question of *what a bunch of text is about*) is done with variations of Latent Semantic Analysis. This alternative model shares the base intuition that if a document or set of documents are about a certain topic, then it's rational to expect some words to be more frequent in it that they otherwise would be. Thus, the count of a word in natural language produced by human beings, or a text, is a relevant indicator of the topicality of that text.

It is, however, apparent that some words are simply more frequent in a given language than other. In english, for example, 'or' is much more common than other words, and anyway texts which don't feature it don't intuitively have different topicality than texts that do: rather, for example, they could be a matter of authorial style or subcultural cultural convention ('however', for example, is probably more used by academics than by other professions). This is why inverse document frequency is used in many NLP techniques, where idf is how many times a particular word appears in a document, and the inverse document frequency of the word across a set of documents. A survey conducted in 2015 showed that 83% of text-based recommender systems in digital libraries use tf–idf (Breitinger et al, 2015).

Another way of ascertaining which words are most important in a text is to compare how many times the term appears in the text with *how many times it appears in the language in general*. Take, for example, Spanish. Very precise data about overall term frequency in language can be obtained, for example, from [1]. If a term is very infrecuent in the generality of Spanish language text, but it appears much less infrequently in a certain corpus of text, then that is probably an indicator of topicality. For example, the word Violín appears in the generality of the Spanish language with a frequency of 9 parts per million. By comparison, it appears with in 1317 ppm for the relevant language's wikipedia page about Bach (151 times more). 'Teclado' (keyboard) has a frequency 288 times what it generally is in spanish, appearing 18 times. In other examples, 'Astronautas' (the plural form of astronaut) appears a whole 1835 more times than expected in the page for the Apollo Program. 'Informático' (the male form of the noun 'informatian', 'computer scientist', 'someone who works in IT' and of the adjective 'related to computers') has a ratio of 248 for the page about Microsoft founder Bill Gates. To my knowledge, this approach has not been widely used. 

This approach is different from tf-idf in that it does not require one to split the text into documents. That is to say, where tf-idf is a measure of the relevance of a term to a document in a set of documents, tf/cf shows how topically relevant a word is in the context of the language a document is uttered in general. tf/cf does not require a set of documents to compare against because it does not rely upon the internal distribution of terms within a corpus but, rather, on the expectation -which works much as a null hypothesis does- that term frequency in a particular document should be similar to the frequency of said term in a much larger corpus. This is justified by the intuition that a sufficiently large and diverse corpus of text in a particular language should not have any particular topicality, as speakers of a language will have used it to talk about a broad enough range of topics.

