from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import numpy as np
import json

app = Flask(__name__)
api = Api(app)


def cleanup_str(row):
    import numpy as np

    temp_list = []
    col_num = 0

    for words in row:
        if (isinstance(words, str)):  # check for NaN values
            c = words.split(',')

            for word in c:
                temp_list.append((word, col_num))

        else:
            temp_list.append((words, col_num))

        col_num += 1

    #         In temp_list --> [(word , column) , ...]
    #                         --> word = word in the column
    #                         --> column = word belonged to this column number in the dataframe

    hash_table = {}

    i = 0

    for element in temp_list:

        if (isinstance(element[0], str)):
            key = hash(element[0].replace(" ", "").lower())

            if (key not in hash_table.keys()):

                hash_table[key] = (element[0], element[1], i)

            else:
                temp_list[hash_table[key][2]] = (np.nan, hash_table[key][1])
                hash_table[key] = (element[0], element[1], i)

        i += 1

    #         In Hash Table -->{(key: word , column , element_number) , ....}

    #         To combine all the words of the same column, so as to obtain the original splitting -
    i = 0
    while (i < len(temp_list)):

        j = i + 1

        temp = temp_list[i][0]

        while (j < len(temp_list) and temp_list[i][1] == temp_list[j][1]):

            if (isinstance(temp_list[i][0], str)):
                del temp_list[i]

            elif (isinstance(temp_list[j][0], str)):
                del temp_list[j]

            else:
                temp += ", " + temp_list[j][0]
                del temp_list[j]

        temp_list[i] = temp

        i += 1

    return temp_list

def filter_word(word):
    if isinstance(word, str):
        word = word.replace(" ", "")
        return word.lower()

def load_vtc():
    df_vtc = pd.read_csv("./india_vtc.csv")
    df_vtc["VTC"] = df_vtc["VTC"].map(filter_word)
    return df_vtc

def replace_city(district):
    district = district.lower()
    district = district.replace("city","")
    return district

def valid_vtc(address):
    df_vtc = load_vtc()
    vtc = filter_word(address[4])
    df_state = df_vtc[df_vtc["VTC"] == vtc]
    row_df_vtc = df_state.shape[0]
    if (row_df_vtc > 0):
        return True
    else:
        return False

def address_filtering(address):
    vtc_status = valid_vtc(address)
    if (vtc_status):
        return address
    else:
        address[4] = np.nan
        return address

def title_case(address):
    address[4] = address[4].title()
    address[5] = address[5].title()
    address[6] = address[6].title()
    return address

class Format(Resource):
    def post(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('building', required=False)  # add args
        parser.add_argument('street', required=False)
        parser.add_argument('landmark', required=False)
        parser.add_argument('locality', required=False)
        parser.add_argument('vtc', required=False)
        parser.add_argument('district', required=False)
        parser.add_argument('state', required=False)
        args = parser.parse_args()  # parse arguments to dictionary

        row = [args["building"], args["street"], args["landmark"], args["locality"], args["vtc"], args["district"]
            , args["state"]]

        row[5] = replace_city(row[5])

        row = cleanup_str(row)
        row = address_filtering(row)
        row = title_case(row)

        row_dict={'building': row[0],
                'street': row[1],
                'landmark': row[2],
                'locality': row[3],
                'vtc': row[4],
                'district': row[5],
                'state': row[6]}

        row_json = json.dumps(row_dict)

        return row_json, 200  # return data with 200 OK


api.add_resource(Format, '/format')  # '/users' is our entry point

if __name__ == '__main__':
    app.run()  # run our Flask app