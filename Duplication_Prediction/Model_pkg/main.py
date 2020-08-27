#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 13:10:53 2020

@author: kellenbullock aka GlobeEater
"""
import pandas as pd
from keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import load_model
import numpy as np

def get_path():
    '''Asks the user for the path to the dataset.'''
    path = input("Please type in the path to the dataset: /Users/path/to/File.xls \n >")
    return path

def load_data(path):
    try:
        df = pd.read_excel(path)
        print("Dataset Loaded.")
        df = df[['OBJECTID','PROPNAME','COUNTYCD', 'RESNAME', 'ADDRESS', 'Lat', 'Long', 'duplicate_check']]
        return df
    except:
        print("The file needs to be a .xlsx or .xls type.")
       
def null_breaker(df, column):
    for column in df:
        df[column] = df[column].fillna(value='NO DATA')
        df[column] = df[column].replace('', "NO DATA")
        df[column] = df[column].replace(' ', "NO DATA")

def no_data(x):
    if x == "99 UNCOLLECTED":
        return "NO DATA"
    elif x == None:
        return "NO DATA"
    elif x == "99 UNCOLLECTED":
        return "NO DATA"
    elif x == "none":
        return "NO DATA"
    else:
        return x

def cleaner(df):
    df['Lat'] = df['Lat'].astype('double')
    df['Long'] = df['Long'].astype('double')
    for column in df:
        try:
            if df[column].dtypes == float:
                df[column] = df[column].astype('double')
        except:
            if df[column].dtypes == object:
                df[column] = df[column].apply(no_data)
                df[column] = df[column].str.lower()
                null_breaker(df, "BLOCK")
            else:
                print("Skipping, because this is an datetime or int type.")
    return df

def tokenize(df):
    '''This method will turn the fields PROPNAME, RESNAME, and ADDRESS into vectors for the machine learning model:
    inputs:
        A pandas dataframe of the Oklahoma landmarks inventory data. This can be from a online database submit form
        or a csv/excel copy of the database.
    outputs:
        A spare matrix array of vectors.
        
    Usage:
        spare_matrix_variable_name = tokenize(df)'''
    propname = df['PROPNAME'].astype(str)
    address = df['ADDRESS'].astype(str)
    resname = df['RESNAME'].astype(str)
    tokenize = Tokenizer(num_words=3000)
    tokenize.fit_on_texts(propname)
    tokenize.fit_on_texts(address)
    tokenize.fit_on_texts(resname)

    x_data = tokenize.texts_to_matrix(propname)
    y_data = tokenize.texts_to_matrix(address)
    z_data = tokenize.texts_to_matrix(resname)

    doneso = np.column_stack((x_data, y_data))
    doneso = np.column_stack((doneso, z_data))
    latso = df['Lat'].values
    longso = df['Long'].values
    doneso = np.column_stack((doneso, latso))
    doneso = np.column_stack((doneso, longso))
    return doneso

def get_prediction(indepdendents, path):
    model = load_model('./Propname_Address_LOCATION_model.h5') # Needs to be changed to my model
    test_frame = pd.read_excel(path)
    test_frame['duplicate_prob'] = ''
    test_frame['duplicate_prob'] = model.predict_proba(indepdendents)
    test_frame['duplicate_prob'] = test_frame['duplicate_prob'].apply(lambda x: (x * 100))
    output_file_path = input("Please provide a path to output the prediction results: ")
    test_frame.to_excel(output_file_path)
    
def main():
    path = get_path()
    df = load_data(path)
    df = cleaner(df)
    indepdendents = tokenize(df)
    get_prediction(indepdendents, path)
    print("Done.")
    
if __name__ == '__main__':
    main()