from flask import Flask
app = Flask(__name__)


@app.route('/<noodles>')
def generateResponse(noodles):
    hasNum = False
    for char in noodles:
        if (char.isdigit()):
            hasNum = True
    if(hasNum):
        cleaned = ""
        for char in noodles:
            if(not char.isdigit()):
                cleaned += char
        return ("Welcome, "+cleaned+", to my CSCB20 website!")
    elif(noodles.islower()):
        return ("Welcome, "+noodles.upper()+", to my CSCB20 website!")
    elif(noodles.isupper()):
        return ("Welcome, "+noodles.lower()+", to my CSCB20 website!")
    else:
        return ("Welcome, "+noodles+", to my CSCB20 website!")


if __name__ == '__main__':
    app.run(debug=True)