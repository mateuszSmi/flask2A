# -*- coding: utf-8 -*-
# quiz/quiz.py

from flask import Flask
from flask import render_template
from flask import request, redirect, url_for, flash

app = Flask(__name__)

# konfiguracja aplikacji
app.config.update(dict(
    SECRET_KEY='bradzosekretnawartosc',
))

# lista pytań
DANE = [{
    'pytanie': 'Stolica Hiszpani, to:',  # pytanie
    'odpowiedzi': ['Madryt', 'Warszawa', 'Barcelona'],  # możliwe odpowiedzi
    'odpok': 'Madryt'},  # poprawna odpowiedź
    {
    'pytanie': 'Objętość sześcianu o boku 6 cm, wynosi:',
    'odpowiedzi': ['36', '216', '18'],
    'odpok': '216'},
    {
    'pytanie': 'Symbol pierwiastka Helu, to:',
    'odpowiedzi': ['Fe', 'H', 'He'],
    'odpok': 'He'},
        {
    'pytanie': 'Wzór na deltę:',
    'odpowiedzi': ['b^2-4ac', '-b/a', '-b/2a'],
    'odpok': 'b^2-4ac'},
]


@app.route('/', methods=['GET', 'POST'])
def index():
    

    if request.method == 'POST':
        punkty = 0
        odpowiedzi = request.form
        
        #return render_template('odpowiedz.html')

        for pnr, odp in odpowiedzi.items():
            if odp == DANE[int(pnr)]['odpok']:
                punkty += 1


        flash('Liczba poprawnych odpowiedzi, to: {0}'.format(punkty))

        return render_template('odpowiedz.html')

    # return 'Cześć, tu Python!'
    return render_template('index.html', pytania=DANE)

#nowy widok
@app.route('/odpowiedz', methods=['GET', 'POST'])
def odpowiedz():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)