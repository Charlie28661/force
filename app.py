from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return 'Let`s guess flagggg!!'


@app.route("/<num>")
def round1(num):

    if int(num) == 864:
        flag1 = '1/2 of flag: THUHC{bbbf0rce_'

        return flag1

    return 'you are guess {}, but it is not the flag!'.format(num)

@app.route("/864/<num>")
def round2(num):

    if int(num) == 1001:
        flag1 = '2/2 of flag: rcce1_}'

        return flag1

    return 'you are guess {}, but it is not the flag!'.format(num)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8600, debug=False)