from processing import master
from error_check import error_checker

from flask import Flask, request, render_template

app = Flask(__name__)
app.config["DEBUG"]=True

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        DNA = str(request.form["DNA"])

        Motif = str(request.form["Motif"])
        results=master(DNA,Motif)
        return render_template("home.html").format(result=results,DNA=DNA,Motif=Motif)



    return render_template("home.html").format(result='', DNA='', Motif='')

@app.route("/errorcheck", methods=["GET", "POST"])
def errorcheck():
    if request.method == "POST":
        DNA = str(request.form["DNA"])


        err_results=error_checker(DNA)
        return render_template("errorcheck.html").format(err_result=err_results,DNA=DNA)



    return render_template("errorcheck.html").format(err_result='', DNA='')



if __name__=='__main__':
    app.run(debug=True)

