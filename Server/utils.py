import pickle
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
all_stopwords = stopwords.words('english')
all_stopwords.remove('not')
ps = PorterStemmer()


__model = None
__cv = None
__prediction = None


def get_prediction(sentiment):
    global __model
    global __cv
    global __prediction
    with open('svm_model_file.pkl', 'rb') as f:
        __model = pickle.load(f)
        print('Model Loaded successfully')
    with open('count_vectorizer.pkl', 'rb') as f:
        __cv = pickle.load(f)
        print('Count Vectorizer Loaded successfully')
    sentiment = re.sub('[^a-zA-Z]', ' ', sentiment)
    sentiment = sentiment.lower()
    sentiment = sentiment.split()
    sentiment = [ps.stem(word) for word in sentiment if not word in set(all_stopwords)]
    sentiment = ' '.join(sentiment)
    bag_of_words = [sentiment]
    new_X_test = __cv.transform(bag_of_words).toarray()
    __prediction = __model.predict(new_X_test)
    __prediction = int(__prediction[0])
    print(__prediction)
    return __prediction
