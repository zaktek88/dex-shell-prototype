const WebSocket = require("ws");
const OpenAI = require("openai");
const readline = require("readline");

// 🔷 Replace with your OpenAI API Key here:
const OPENAI_API_KEY = "your-openai-api-key-here";

// Initialize OpenAI client (v4+)
const openai = new OpenAI({ apiKey: OPENAI_API_KEY });

// Launch WebSocket server
const wss = new WebSocket.Server({ port: 8080 });
console.log("✅ Dex Bridge listening on ws://localhost:8080");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

wss.on("connection", (ws) => {
  console.log("🤖 Dex Agent connected.");

  ws.on("message", (data) => {
    console.log(`📥 Dex Agent replied:\n${data.toString()}`);
  });

  ws.on("close", () => {
    console.log("❌ Dex Agent disconnected.");
  });

  askPrompt();

  function askPrompt() {
    rl.question("\n💬 What do you want Dex to do? ", async (userInput) => {
      try {
        const gptResponse = await openai.chat.completions.create({
          model: "gpt-4o",
          messages: [
            {
              role: "system",
              content: `You are Dex, an AI assistant controlling a device through a shell. Respond ONLY with shell commands prefixed with 'shell:' or memory commands ('remember key value', 'recall key').`,
            },
            { role: "user", content: userInput },
          ],
        });

        const reply = gptResponse.choices[0].message.content.trim();
        console.log(`🧠 Dex thinks:\n${reply}`);

        ws.send(reply);

        askPrompt(); // loop
      } catch (err) {
        console.error("❌ Error from OpenAI:", err.message);
        askPrompt();
      }
    });
  }
});
