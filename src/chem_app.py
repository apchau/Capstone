from flask import Flask, jsonify
import platform
import pandas as pd
import numpy as np
from flask import abort, make_response
import json

app = Flask(__name__)


def get_list_chem_dicts():
    with open('chemicals.json') as json_data:
        chemical_list = json.load(json_data)
        return chemical_list


chemicals = get_list_chem_dicts()

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'chemicals': chemicals})

@app.route('/todo/api/v1.0/tasks/<string:CAS>', methods=['GET'])
def get_chemical_CAS(CAS):
    chemical = [chemical for chemical in chemicals if chemical['CAS#:'] == CAS]
    chemicalname = [chemicalname for chemicalname in chemicals if chemicalname['Chemical Name:'] == CAS]
    if ((len(chemical) == 0) and (len(chemicalname) == 0)):
        abort(404)
    if (len(chemical) > 0):
        return jsonify({'chemical': chemical[0]})
    elif (len(chemicalname) > 0):
        return jsonify({'chemicalname': chemicalname[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
