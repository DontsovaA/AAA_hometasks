if __name__ == '__main__':

    class CountVectorizer:
        features = []

        def get_feature_names(self):
            return self.features

        def __features_init__(self, data : list):
            for strok in data:
                strok = strok.lower()
                words = strok.split(' ')
                for word in words:
                    if word not in self.features:
                        self.features.append(word)

        def fit_transform(self, data : list):
            data_length = len(data)
            self.__features_init__(data)
            self.count_matrix = [len(self.features)*[0] for i in range(data_length)]
            j = 0
            for strok in data:
                strok = strok.lower()
                words = strok.split(' ')
                for word in words:
                    for i in range(len(self.features)):
                        if word == self.features[i]:
                            self.count_matrix[j][i] +=1
                            break
                j = j+1
            return self.count_matrix

#проверка работы                                                                                                                                                                                                                                                                                                                        
    corpus = [ 'Crock Pot Pasta Never boil pasta again', 'Pasta Pomodoro Fresh ingredients Parmesan to taste' ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
                                                                                                                                                                                                                                                                                                            
