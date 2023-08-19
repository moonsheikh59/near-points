import geopy.distance as gd
import json
from urllib.request import urlopen

from flask import Flask,render_template


app = Flask(__name__)

@app.route('/')
def home():

    url = "https://api.npoint.io/f26432e9e880999eeb1b"

    response = urlopen(url)
    data_json = json.loads(response.read())
    new = []
    features = data_json["features"]

    for i in range(len(features)):
        new.append(features[i]["geometry"]["coordinates"])
    print(new)
    red = []
    blue = []

    for a in range(0,len(new)-1):
        for b in range(a+1,len(new)):
            x1 = new[a][1]
            y1 = new[a][0]
            x2 = new[b][1]
            y2 = new[b][0]
            result = gd.distance((x1,y1), (x2,y2)).km


            if result <= 90.00:

                if new[a] not in blue:
                    red.append(new[a])

                else:
                    blue.remove(new[a])

                if new[b] not in blue:
                    red.append(new[b])

                else:
                    blue.remove(new[b])

            else:
                if new[a] not in red:
                    blue.append(new[a])

                if new[b] not in red:
                    blue.append(new[b])

            print("red",red)
            print("blue",blue)

    return render_template('index-1.html', red=red, blue=blue)


if __name__ == "__main__":
    app.run(debug=True)