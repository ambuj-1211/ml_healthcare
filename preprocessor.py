import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pickle
import spacy
# preprocessor.py file to get the text and clean it and vectorize it and return the vectorized array
class preprocessor:
    def __init__(self):
        self.ps=PorterStemmer()
        self.nlp = spacy.load('en_core_web_sm')
        # self.stop_words = set(stopwords.words('english'))

    def cleaning_string(self,data): 
            review= re.sub('[^a-zA-Z]',' ',data)
            review = review.lower()
            review = review.split()

            review= [self.ps.stem(word) for word in review if word not in stopwords.words('english')]
            review= ' '.join(review)
            return review

    def vectorize(self,data) :
        tfidf=pickle.load(open('tfidf_vectorizer.pkl','rb'))
        ls=[]
        ls.append(data)
        vectorized_array = tfidf.transform(ls).toarray()
        return vectorized_array

    def forward(self,data):
        data1 = self.cleaning_string(data)
        data = self.vectorize(data1)
        return data

# if __name__=='__main__':
#     p1=preprocessor()
#     p1.forward('My hand is very much paining and the pain pertains to be continued till the end of the project so I can not give any inupt in the project so we call some on stage the name is very sensational')
#     print(p1)
