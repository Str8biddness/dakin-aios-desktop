import React, { useState } from 'react';

const TerminalPanel: React.FC = () => {
  const [command, setCommand] = useState('');
  const [output, setOutput] = useState('');

  const execute = async () => {
    const res = await fetch('/api/terminal', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Authorization: 'Bearer key1' },
      body: JSON.stringify({ command }),
    });
    const data = await res.json();
    setOutput(data.output);
  };

  return (
    <div>
      <h2>Terminal Panel</h2>
      <input value={command} onChange={(e) => setCommand(e.target.value)} />
      <button onClick={execute}>Execute</button>
      <pre>{output}</pre>
    </div>
  );
};

export default TerminalPanel;
