import numpy as np

class CountVectorizer:
  features = []
  def __init__(self):
    pass
                    
  def get_feature_names(self):
    return self.features
                                    
  def __features_init__(self, data):
    for strok in data:
      strok = strok.lower()
      words = strok.split(" ")
      for word in words:
        if word not in self.features:
          self.features.append(word)                                                     
    return
           
  def fit_transform(self, data):
    n = len(data)
    self.__features_init__(data)
    self.count_matrix = np.zeros((n, len(self.features)))
    j = 0
    for strok in data:
      strok = strok.lower()
      words = strok.split(" ")
      for word in words:
        for i in range(len(self.features)):
          if word == self.features[i]:
            self.count_matrix[j,i] +=1
            break
      j = j+1
    return self.count_matrix
    
    
corpus = [ 'Crock Pot Pasta Never boil pasta again', 'Pasta Pomodoro Fresh ingredients Parmesan to taste' ]
vectorizer = CountVectorizer() 
count_matrix = vectorizer.fit_transform(corpus) 
print(vectorizer.get_feature_names()) 
print(count_matrix)
