import pandas as pd 

# File with all the functions needed to clean the dataset

def new_color(serie, color1, color2):
    '''
    Function that takes the old color column
    and sorts it again.
    input = dataframe serie, two lists of colors
    output = dataframe serie
    '''
    new_color = []
    for d in serie:
        if d in color1:
            e = d.replace(d, "C")
            new_color.append(e)
        elif d in color2:
            f = d.replace(d, "NC")
            new_color.append(f)
        else:
            g = d.replace(d, 'Other')
            new_color.append(g)
    df = pd.DataFrame(new_color, columns={'colorless'})
    return df


def new_clarity(serie, cl1, cl2, cl3, cl4, cl5):
    '''
    Function that takes the old clarity column
    and sorts it again.
    input = dataframe serie, lists of clarities
    output = dataframe serie
    '''
    new_clarity = []
    for d in serie:
        if d in cl1:
            e = d.replace(d, "IF")
            new_clarity.append(e)
        elif d in cl2:
            f = d.replace(d, "VVS")
            new_clarity.append(f)
        elif d in cl3:
            g = d.replace(d, "VS")
            new_clarity.append(g)
        elif d in cl4:
            h = d.replace(d, "SI")
            new_clarity.append(h)
        elif d in cl5:
            i = d.replace(d, "I")
            new_clarity.append(i)
        else:
            j = d.replace(d, 'Other')
            new_clarity.append(j)
    df = pd.DataFrame(new_clarity, columns={'clariness'})
    return df


def concating(lst):
    '''
    Function that concatenates multiples dataframes.
    input = list of dataframes
    output = final dataframe
    '''
    new_data = pd.concat(lst, axis=1)
    return new_data


def droping(data, lst):
    '''
    Function to drop muliples columns.
    input = dataframe, list of columns to drop.
    output = final dataframe
    '''
    new_data = data.drop(lst, axis=1)
    return new_data