import json
import pickle
import numpy as np
__locactions = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0],2)


def get_location_names():
    return __locactions
 
def load_saved_artifacts():
    print("Loading saved artifacts .... start")
    global __data_columns
    global __locactions

    with open("C:/Manav/Home/PredictingHousePrice/server/artifacts/Columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locactions = __data_columns[3:]

    global __model
    with open("C:/Manav/Home/PredictingHousePrice/server/artifacts/bengaluru_house_prices_model.pickel",'rb') as f:
        __model = pickle.load(f)
    print("Loading saved Artifacts .....Done")

if __name__=="__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000,3,3))
    print(get_estimated_price('1st Phase JP Nagar',1000,2,3))
    print(get_estimated_price('Kalhalli',1000,2,2))
    print(get_estimated_price('Ejipura',1000,2,2))