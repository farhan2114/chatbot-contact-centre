import React, { useState, useRef, useEffect } from "react";
import "./Chatbot.css";

function detectIntent(message) {
  const lower = message.toLowerCase();
  if (/\bhi\b|\bhello\b|\bhey\b/.test(lower)) return "greeting";
  if (/\bbill\b|\bpayment\b|\bcharge\b/.test(lower)) return "billing";
  if (/\bproblem\b|\bcomplain\b|\bissue\b/.test(lower)) return "complaint";
  if (/\bproduct\b|\bservices\b|\bplan\b/.test(lower)) return "product";
  if (/\bhour\b|\btime\b|\bopen\b/.test(lower)) return "hours";
  return "fallback";
}

const responses = {
  greeting: ["Hello! How can I help you today?", "Hi! Need any assistance?"],
  billing: ["Please share your billing ID to proceed."],
  complaint: ["I'm sorry to hear that. Please describe your issue."],
  product: ["We offer broadband, TV, and mobile services."],
  hours: ["We’re open from 9 AM to 6 PM, Monday to Saturday."],
  fallback: ["Sorry, I didn't understand that. Can you rephrase?"]
};

function Chatbot() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const chatEndRef = useRef(null);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleSend = () => {
    if (!input.trim()) return;
    const userMessage = { sender: "user", text: input };
    const intent = detectIntent(input);
    const reply = {
      sender: "bot",
      text: responses[intent][Math.floor(Math.random() * responses[intent].length)]
    };
    setMessages((prev) => [...prev, userMessage, reply]);
    setInput("");
  };

  return (
    <div className="chat-container">
      <h2>Contact Centre Chatbot</h2>
      <div className="chat-box">
        {messages.map((msg, idx) => (
          <div key={idx} className={`message ${msg.sender}`}>
            {msg.sender === "user" ? "You" : "Bot"}: {msg.text}
          </div>
        ))}
        <div ref={chatEndRef}></div>
      </div>
      <div className="input-area">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your message..."
          onKeyDown={(e) => e.key === "Enter" && handleSend()}
        />
        <button onClick={handleSend}>Send</button>
      </div>
    </div>
  );
}

export default Chatbot;
