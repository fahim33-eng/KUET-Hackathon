"use client";

import React, { useState } from 'react';

function Chatbot() {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');

  const ENDPOINT = process.env.NEXT_PUBLIC_ENDPOINT

  const handleSendMessage = async () => {
    try {
      const res = await fetch(`${ENDPOINT}/chatbot`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message }),
      });
      const data = await res.json();
      setResponse(data.reply);
      setMessage('');
    } catch (error) {
      console.error('Error sending message:', error);
    }
  };

  return (
    <div>
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Ask the chatbot"
      />
      <button onClick={handleSendMessage}>Send</button>
      <p>Response: {response}</p>
    </div>
  );
}

export default Chatbot;