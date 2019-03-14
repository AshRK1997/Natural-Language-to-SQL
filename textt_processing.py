class text_nlp():


    def nl_process(self,txt):

        success = False
        stemmed_txt="empty"
        try:
            import nltk

            success = True
        except ImportError:
            print("nltk module is missing. Please install it")


        if success:
            lowercase_txt = txt.lower()
            tokenized_txt = nltk.tokenize.word_tokenize(lowercase_txt)
            stop_words = set(nltk.corpus.stopwords.words('english'))
            filtered_txt = [w for w in tokenized_txt if not w in stop_words]
            stemmed_txt = []
            stemmer = nltk.stem.SnowballStemmer('english')
            for w in filtered_txt:
                stemmed_txt.append(stemmer.stem(w))
        return success,stemmed_txt


