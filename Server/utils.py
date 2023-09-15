import pickle

__model = None

def get_prediction(sentiment):
    global __model
    with open('svm_model_file.pkl', 'rb') as f:
        __model = pickle.load(f)
        print('Model Loaded successfully')

    return sentiment
