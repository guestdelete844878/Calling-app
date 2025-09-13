<!DOCTYPE html>
<html>
<head>
  <title>WebRTC + Flask Signaling</title>
  <script src="https://cdn.socket.io/4.5.4/socket.io.min.js"></script>
</head>
<body>
  <h2>📞 WebRTC Call</h2>
  <button onclick="joinRoom('497405')">Join Room 497405</button>
  <button onclick="joinRoom('84936')">Join Room 84936</button>

  <h3>Local</h3>
  <video id="localVideo" autoplay playsinline muted></video>
  <h3>Remote</h3>
  <video id="remoteVideo" autoplay playsinline></video>

  <script>
    const socket = io();
    let pc, localStream;
    const servers = { iceServers: [{ urls: "stun:stun.l.google.com:19302" }] };

    async function joinRoom(roomId) {
      console.log("Joining Room:", roomId);

      localStream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
      document.getElementById("localVideo").srcObject = localStream;

      pc = new RTCPeerConnection(servers);
      localStream.getTracks().forEach(track => pc.addTrack(track, localStream));

      pc.ontrack = e => document.getElementById("remoteVideo").srcObject = e.streams[0];

      pc.onicecandidate = e => {
        if (e.candidate) {
          socket.emit('signal', { room: roomId, candidate: e.candidate });
        }
      };

      const offer = await pc.createOffer();
      await pc.setLocalDescription(offer);
      socket.emit('signal', { room: roomId, offer });

      socket.on('signal', async data => {
        if (data.offer) {
          await pc.setRemoteDescription(new RTCSessionDescription(data.offer));
          const answer = await pc.createAnswer();
          await pc.setLocalDescription(answer);
          socket.emit('signal', { room: roomId, answer });
        } else if (data.answer) {
          await pc.setRemoteDescription(new RTCSessionDescription(data.answer));
        } else if (data.candidate) {
          await pc.addIceCandidate(new RTCIceCandidate(data.candidate));
        }
      });
    }
  </script>
</body>
</html>
