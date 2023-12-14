from flask import jsonify, make_response

def ok(values, massage):
    res={
        'values' : values,
        'massage' : massage
    }

    return make_response(jsonify(res)),200

def badRequest(values, massage):
    res={
        'values' : values,
        'massage' : massage
    }
    return make_response(jsonify(res)),400