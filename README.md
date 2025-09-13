<!DOCTYPE html>
<html>
<head>
  <title>WebRTC Fixed</title>
  <script src="https://cdn.socket.io/4.5.4/socket.io.min.js"></script>
</head>
<body>
  <h2>📞 WebRTC Call</h2>
  <button onclick="joinRoom()">Join Call</button>

  <h3>Local</h3>
  <video id="localVideo" autoplay playsinline muted></video>
  <h3>Remote</h3>
  <video id="remoteVideo" autoplay playsinline></video>

  <script>
    const socket = io(); // Make sure your Flask server is running
    let pc, localStream;
    const ROOM_ID = '58740';
    const servers = { iceServers: [{ urls: "stun:stun.l.google.com:19302" }] };

    // Only listen once
    socket.on('signal', async data => {
      if (!pc) return;
      if (data.offer && !pc.currentRemoteDescription) {
        await pc.setRemoteDescription(new RTCSessionDescription(data.offer));
        const answer = await pc.createAnswer();
        await pc.setLocalDescription(answer);
        socket.emit('signal', { room: ROOM_ID, answer });
      } else if (data.answer && !pc.currentRemoteDescription?.type) {
        await pc.setRemoteDescription(new RTCSessionDescription(data.answer));
      } else if (data.candidate) {
        try {
          await pc.addIceCandidate(new RTCIceCandidate(data.candidate));
        } catch (err) {
          console.error("Error adding candidate:", err);
        }
      }
    });

    async function joinRoom() {
      console.log("Joining Room:", ROOM_ID);

      // Get camera and mic
      localStream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
      document.getElementById("localVideo").srcObject = localStream;

      // Peer connection
      pc = new RTCPeerConnection(servers);
      localStream.getTracks().forEach(track => pc.addTrack(track, localStream));

      pc.ontrack = e => document.getElementById("remoteVideo").srcObject = e.streams[0];

      pc.onicecandidate = e => {
        if (e.candidate) socket.emit('signal', { room: ROOM_ID, candidate: e.candidate });
      };

      // Only create offer if no remote description
      const offer = await pc.createOffer();
      await pc.setLocalDescription(offer);
      socket.emit('signal', { room: ROOM_ID, offer });
    }
  </script>
</body>
</html>
