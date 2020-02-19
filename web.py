from flask import Flask, request, render_template
from app import tm_api
import json

app = Flask(__name__)


@app.route('/form-example', methods=['GET', 'POST']) #allow both GET and POST requests
def form_example():
    if request.method == 'POST':
        location = request.form.get('location')
        date = request.form.get('date')
        category = request.form.get('category')
        radius = request.form.get('radius')
        list_of_events = tm_api(location, date, category, radius);
        return render_template('index.html', lst=list_of_events);
    return render_template('index.html');

    # '''<form method="POST">
    #             City: <input type="text" name="city"><br>
    #             Date: <input type="text" name="date"><br>
    #             Keyword: <input type="text" name="keyword"><br>
    #             Radius: <input type="text" name="radius"><br>
    #             <input type="submit" value="Submit"><br>
    #         </form>''';

    # uncomment the line below after finishing the form-example demo
    # return render_template('index.html')


if __name__ == '__main__':
    app.run()
