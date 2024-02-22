import flask
from flask import jsonify, request
from flask_cors import CORS
import os
from firebase import StorageImgFirebase
from CancerDetectionModelImp import CancerDetectionModelImp

app = flask.Flask(__name__)
CORS(app)


@app.route("/cancerdetection", methods=["GET", "POST"])
def get_Pdf():
    if request.method == "POST":
        data = request.get_json()
        nameImg = data.get("nameImg")
        imgpath = "img/" + nameImg
        # imgpath = "/img/img1.jpg"
        objFire = StorageImgFirebase()
        urlimg = objFire.DownloadUrl(imgpath)
        moedel = CancerDetectionModelImp()
        value = moedel.predictClassFoTheImagUrl(urlimg)

        return jsonify({"url": value})
    else:

        return jsonify({"reponce": "Api work!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
