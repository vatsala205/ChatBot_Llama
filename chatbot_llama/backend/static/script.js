console.log("script.js loaded");
async function sendMessage() {
  console.log("sendMessage called");
  const inputBox = document.getElementById('user-input');
  const message = inputBox.value.trim();
  if (!message) return;

  const chatBox = document.getElementById('chat-box');
  chatBox.innerHTML += `<div class="user-msg"><b>You:</b> ${message}</div>`;

  inputBox.value = '';

  const response = await fetch('/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message }),
  });

  const data = await response.json();
  chatBox.innerHTML += `<div class="bot-msg"><b>Bot:</b> ${data.reply}</div>`;

  chatBox.scrollTop = chatBox.scrollHeight;
}
