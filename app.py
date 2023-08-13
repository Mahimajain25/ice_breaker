from flask import Flask, render_template, request, jsonify

from icebreaker import ice_break

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process",method=["POST"])
def process():
    name = request.form["name"]
    person_info, profile_pic_url = ice_break(name=name)

    return jsonify(
        {
            "summary": person_info.summary,
            "interest": person_info.topic_of_interest,
            "facts": person_info.facts,
            "ice_beaker": person_info.ice_breaker,
            "picture_url": profile_pic_url,
        }
    )


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)