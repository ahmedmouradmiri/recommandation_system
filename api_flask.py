import json
from flask import Flask , request , jsonify
from recommandation import cleaning
clean=cleaning()
app= Flask(__name__)
@app.route("/recommandation",methods= ["POST"])
def predict():
    json_=request.get_data(as_text=True)
    query_df=str(json_)
    prediction=clean.recommandation(query_df)
    return prediction
if __name__== "__main__":
    app.run(debug=True)
