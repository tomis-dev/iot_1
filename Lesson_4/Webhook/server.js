import express, { response } from "express";

const app = express();
const PORT = 3000;

const DISCORD_WEBHOOK_URL = "xxxx";

app.use(express.json());

app.post("/notify", (req, res) => {
  const { message } = req.body;

  if (!message) {
    return res.status(400).json({ error: "Message is required" });
  }
  fetch(DISCORD_WEBHOOK_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ content: message }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error(`Discord responded with status ${response.status}`);
      }
      res.json({ status: "Message sent..." });
    })
    .catch((error) => {
      console.error("Error sending to Discord");
      res.status(500).json({ error: "Failed sending your message" });
    });
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
