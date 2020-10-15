# Nasłuchuje na webhooki
# Instalacja: python3 -m pip install Flask
# Uruchomienie: python3 -m flask run --host=0.0.0.0
# Wywołanie ze strony klienta: http://monitoring.example.com:5000/restartmeye

from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/restartmeye', methods=['GET'])
def respond():
    print(request.json);
    return Response(status=200)
