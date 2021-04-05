from flask import Flask, request, Response
import os

app = Flask(__name__)

@app.route('/restartmeye', methods=['GET'])
def respond_restart():
    print(request.json);
    stream = os.popen('/usr/sbin/runuser -l sa-motioneye -c "/usr/bin/docker restart motioneye"')
    output = stream.read()
    print(output)
    return Response(status=200)

@app.route('/kopiuj', methods=['GET'])
def respond_kopiuj():
    print(request.json);
    dzien = request.args.get('dzien')
    godzina = request.args.get('godzina')
    stream = os.popen('echo '+ dzien +'h:' + godzina + '  > /tmp/kopiujco.txt')
    output = stream.read()
    print(dzien)
    return Response(status=200)
