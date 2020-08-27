# State Historical Preservation Office's Oklahoma Landmarks Inventory Database

## Background:

<p>This tool was designed to help reduce the amount of redunant information within
the Oklahoma Landmarks Inventory database.</p>

<p>This model was trained using the PROPNAME, RESNAME, ADDRESS, Lat, and Long
fields.</p>

## Setup:
<p>To recreate the virtual enviroment this code is intended to run in please use the 
following commands in the anaconda powershell:</p>

'''
conda env create -f environment.yml
'''

<p>To verify the new enviroment was installed correctly use:</p>

'''
conda env list
'''

## Input, Output:

<p>This program takes in a spreadsheet of records either existing from the OLI or
new data, and outputs a new spreadsheet with a duplication_proability field. </p>

## Usage:

<ol>
    <li>The setup step must be completed prior to using the program.</li>
    <li>The virutal enviroment must then be activated by using the command:</li>
    '''
    conda activate SHPO
    '''
    <li>The active working directory must be in the same folder as the program.</li>
    <li>Then the program can be run by using the command:</li>
    '''
    python main.py
    '''
    <li>The user will be prompted with a request for input data. The absolute pathway
    must be provided.</li>
    '''
    Please provide a path to the dataset: C/:/Users/me/Desktop/datafolder/Alfalfa - Matthew's Copy.xlsx
    '''
    <li>The program will then prompt the user with a location to store the dataset.</li>
    '''
    Please provide a path to output the prediction results: ///C:/Users/me/Desktop/Outputs/Alfalfa.xlsx
    '''
</ol>

