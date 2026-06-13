$(document).ready(function () {
  const welcome = "Hi! I'm your Student Success Assistant. Ask me anything about careers, internships, placements, learning resources, or student life!";
  appendMessage("bot", welcome);

  $("#userInput").on("keypress", function (e) {
    if (e.which === 13) sendMessage();
  });

  $("#sendBtn").on("click", function () {
    sendMessage();
  });

  $(".pill").on("click", function () {
    const text = $(this).data("msg");
    $("#userInput").val(text);
    sendMessage();
  });
});

function sendMessage() {
  const userText = $("#userInput").val().trim();
  if (!userText) return;

  appendMessage("user", userText);
  $("#userInput").val("");

  const typingId = showTyping();

  $.post("/get", { msg: userText }, function (data) {
    removeTyping(typingId);
    appendMessage("bot", data.response);
  }).fail(function () {
    removeTyping(typingId);
    appendMessage("bot", "Something went wrong. Please try again.");
  });
}

function appendMessage(sender, text) {
  const avatar = sender === "bot" ? "🎓" : "You";
  const msgHtml = `
    <div class="message ${sender}">
      <div class="avatar">${avatar}</div>
      <div class="bubble">${formatText(text)}</div>
    </div>`;
  $("#chatbox").append(msgHtml);
  scrollToBottom();
}

function formatText(text) {
  return text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
    .replace(/\*(.*?)\*/g, "<em>$1</em>")
    .replace(/\n/g, "<br>");
}

function showTyping() {
  const id = "typing-" + Date.now();
  const html = `
    <div class="message bot typing" id="${id}">
      <div class="avatar">🎓</div>
      <div class="bubble">
        <div class="typing-dots">
          <span></span><span></span><span></span>
        </div>
      </div>
    </div>`;
  $("#chatbox").append(html);
  scrollToBottom();
  return id;
}

function removeTyping(id) { $("#" + id).remove(); }

function scrollToBottom() {
  const chatbox = $("#chatbox")[0];
  chatbox.scrollTop = chatbox.scrollHeight;
}