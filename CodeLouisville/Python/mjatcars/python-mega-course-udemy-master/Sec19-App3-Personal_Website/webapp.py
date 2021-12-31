from flask import Flask  #Import Flask object
#localhost:5000

app=Flask(__name__) #Instantiate Flask object

@app.route('/')
def home():
    return "website2 contents belongs here!"

@app.route('/about/')
def about():
    return "About here!"


if __name__=="__main__": #Assign name main to file
    app.run(debug=True)
