import React, { useState } from 'react';
import io from 'socket.io-client';

const socket = io('http://localhost:5000');

const ChatPanel: React.FC = () => {
  const [message, setMessage] = useState('');
  const [responses, setResponses] = useState<string[]>([]);

  const sendMessage = () => {
    socket.emit('chat', message);
    socket.on('response', (res: string) => setResponses([...responses, res]));
  };

  return (
    <div>
      <h2>Chat Panel</h2>
      <input value={message} onChange={(e) => setMessage(e.target.value)} />
      <button onClick={sendMessage}>Send</button>
      <ul>{responses.map((r, i) => <li key={i}>{r}</li>)}</ul>
    </div>
  );
};

export default ChatPanel;
