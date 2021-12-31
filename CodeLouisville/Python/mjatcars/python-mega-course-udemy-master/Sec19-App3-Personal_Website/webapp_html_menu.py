from flask import Flask, render_template #Import Flask objects
#localhost:5000

app=Flask(__name__) #Instantiate Flask object

#Home page
@app.route('/')
def home():
    return render_template("home.html")

#About page
@app.route('/about/')
def about():
    return render_template("about.html")


if __name__=="__main__": #Assign name "main" to file
    app.run(debug=True)
