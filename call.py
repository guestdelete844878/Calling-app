from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template("index.html")

@socketio.on('join')
def handle_join(data):
    room = data['room']
    join_room(room)
    emit('joined', {"msg": f"User joined room {room}"}, room=room)

@socketio.on('signal')
def handle_signal(data):
    room = data['room']
    emit('signal', data, room=room, include_self=False)

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)