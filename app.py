from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/check_name', methods=['GET'])
def check_name():
    input_name = request.args.get('name')

    if input_name == "hello":
        result = "hello, how are you?"
    elif input_name == "good":
        result = "ok have a good day!"
    elif input_name == "bad":
        result = "oh, thats not good, let's hope it get better!"
    elif input_name == "no!":
        result = "I do not know what your 'no'ing about but, NNNNNNOOOOOOO!!!!!"
    else:
        result = "ERROR: Responce not found!"

    return result

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
