const express = require("express");
const { WebSocketServer } = require("ws");

const app = express();

// Railway ya Heroku jaisi services PORT env variable deti hain
const PORT = process.env.PORT || 0; // 0 = Node.js khud free port pick karega

const server = app.listen(PORT, () => {
  const address = server.address();
  console.log(`✅ Server running on http://localhost:${address.port}`);
});

app.use(express.static("public"));

const wss = new WebSocketServer({ server });
wss.on("connection", (ws) => {
  ws.on("message", (msg) => {
    wss.clients.forEach((client) => {
      if (client !== ws && client.readyState === client.OPEN) {
        client.send(msg.toString());
      }
    });
  });
});