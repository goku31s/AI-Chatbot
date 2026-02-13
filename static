const chatBox = document.getElementById("chat-box");
const sessionList = document.getElementById("session-list");
const newSessionBtn = document.getElementById("new-session");

// Store sessions in memory
let sessions = [];
let currentSession = null;

// Add a new chat message
function addMessage(content, sender) {
  const div = document.createElement("div");
  div.className = "message " + sender;
  div.innerHTML = content;
  chatBox.appendChild(div);
  chatBox.scrollTop = chatBox.scrollHeight;

  if (currentSession) {
    currentSession.messages.push({ sender, content });
  }
}

// Typing effect for AI messages
function typeMessage(content, sender) {
  const div = document.createElement("div");
  div.className = "message " + sender;
  chatBox.appendChild(div);
  let i = 0;

  function type() {
    if (i < content.length) {
      div.innerHTML += content.charAt(i);
      i++;
      chatBox.scrollTop = chatBox.scrollHeight;
      setTimeout(type, 15);
    }
  }
  type();

  if (currentSession) {
    currentSession.messages.push({ sender, content });
  }
}

// Render sessions with three-dot menu
function renderSessions() {
  sessionList.innerHTML = "";
  sessions.forEach((session, index) => {
    const li = document.createElement("li");
    li.className = "session-item";

    // Session name
    const nameSpan = document.createElement("span");
    nameSpan.textContent = session.name;
    nameSpan.className = "session-name";
    nameSpan.addEventListener("click", () => switchSession(index));

    // Three-dot menu
    const menuBtn = document.createElement("span");
    menuBtn.innerHTML = "⋮";
    menuBtn.className = "session-menu";
    menuBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      toggleMenu(index, menuBtn);
    });

    li.appendChild(nameSpan);
    li.appendChild(menuBtn);
    sessionList.appendChild(li);
  });
}

// Toggle session menu (rename + delete)
function toggleMenu(index, menuBtn) {
  // Remove existing popups
  document.querySelectorAll(".session-menu-popup").forEach(popup => popup.remove());

  const popup = document.createElement("div");
  popup.className = "session-menu-popup";

  // Rename option
  const renameOption = document.createElement("div");
  renameOption.textContent = "Rename";
  renameOption.addEventListener("click", (e) => {
    e.stopPropagation();
    const newName = prompt("Enter new session name:", sessions[index].name);
    if (newName && newName.trim() !== "") {
      sessions[index].name = newName.trim();
      renderSessions();
    }
    popup.remove();
  });
  popup.appendChild(renameOption);

  // Delete option
  const deleteOption = document.createElement("div");
  deleteOption.textContent = "Delete";
  deleteOption.addEventListener("click", (e) => {
    e.stopPropagation();
    deleteSession(index);
    popup.remove();
  });
  popup.appendChild(deleteOption);

  menuBtn.parentElement.appendChild(popup);

  function closePopup(event) {
    if (!popup.contains(event.target) && event.target !== menuBtn) {
      popup.remove();
      document.removeEventListener("click", closePopup);
    }
  }

  setTimeout(() => {
    document.addEventListener("click", closePopup);
  }, 0);
}

// Switch to session
function switchSession(index) {
  currentSession = sessions[index];
  chatBox.innerHTML = "";
  currentSession.messages.forEach(msg => addMessage(msg.content, msg.sender));
}

// Delete session
function deleteSession(index) {
  const isCurrent = currentSession === sessions[index];
  sessions.splice(index, 1);

  if (sessions.length === 0) {
    const firstSession = { name: "Session 1", messages: [] };
    sessions.push(firstSession);
    currentSession = firstSession;
    chatBox.innerHTML = "";
  } else if (isCurrent) {
    currentSession = sessions[0];
    chatBox.innerHTML = "";
    currentSession.messages.forEach(msg => addMessage(msg.content, msg.sender));
  }

  renderSessions();
}

// Create new session
newSessionBtn.addEventListener("click", () => {
  const sessionName = `Session ${sessions.length + 1}`;
  const newSession = { name: sessionName, messages: [] };
  sessions.push(newSession);
  currentSession = newSession;
  chatBox.innerHTML = "";
  renderSessions();
});

// Send user input
document.getElementById("chat-form").addEventListener("submit", function (event) {
  event.preventDefault();
  const userInput = document.getElementById("user-input").value.trim();
  if (!userInput) return;

  addMessage(userInput, "user");
  document.getElementById("user-input").value = "";

  // Simulated AI response (replace with real API call)
  fetch(`/chat?user_input=${encodeURIComponent(userInput)}`)
    .then(response => response.json())
    .then(data => {
      typeMessage(data.content, "ai");
    })
    .catch(error => {
      console.error("Error fetching AI response:", error);
      typeMessage("Error: Unable to fetch response.", "ai");
    });
});

// Initialize first session
(() => {
  const firstSession = { name: "Session 1", messages: [] };
  sessions.push(firstSession);
  currentSession = firstSession;
  renderSessions();
})();
