from flask import Flask, request, session, render_template

from PyNet.OSPF import draw_ospf, generate_ospf

app = Flask(__name__)
app.secret_key = '151ROCKS!'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # check if input is valid
        if request.form['routers'].isdigit() == False:
            return render_template('index.html', error="Invalid input! Make Sure You Enter a Number!")
        elif int(request.form['routers']) <= 0 or int(request.form['routers']) > 30:
            return render_template('index.html', error="Invalid input! The number your entered will not work!")
        routers = int(request.form['routers'])
        session['routers'] = routers
        draw_ospf(*generate_ospf(routers, 0, 0))
        return render_template('map.html')
    return render_template('index.html')


@app.route('/map', methods=['GET', 'POST'])
def ospf_map():
    if request.method == 'POST':
        routers = request.form.get('routers', 0) or session['routers']
        session['routers'] = routers  # Store it in session
        routers = int(routers)
        start = request.form['starting'] or 0
        end = request.form['ending'] or 0
        start = int(start)
        end = int(end)
        print(start, end)

        if start > routers or end > routers or start < 0 or end < 0:
            return render_template('map.html', error="Invalid input! Starting or ending router is not in the network!")
        draw_ospf(*generate_ospf(routers, start, end))
        return render_template('map.html')

    return render_template('map.html')


if __name__ == '__main__':
    app.run(debug=True)
