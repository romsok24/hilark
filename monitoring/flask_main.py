from flask import Flask, request, Response
import os

app = Flask(__name__)

@app.route('/restartmeye', methods=['GET'])
def respond():
    print(request.json);
    stream = os.popen('/usr/sbin/runuser -l <username> -c "/usr/bin/docker restart <container>"')
    output = stream.read()
    print(output)
    return Response(status=200)
