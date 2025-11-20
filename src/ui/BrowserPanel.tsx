import React, { useState } from 'react';

const BrowserPanel: React.FC = () => {
  const [url, setUrl] = useState('');
  const [summary, setSummary] = useState('');

  const analyze = async () => {
    const res = await fetch('/api/browser', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Authorization: 'Bearer key1' },
      body: JSON.stringify({ url }),
    });
    const data = await res.json();
    setSummary(data.summary);
  };

  return (
    <div>
      <h2>Browser Panel</h2>
      <input value={url} onChange={(e) => setUrl(e.target.value)} />
      <button onClick={analyze}>Analyze</button>
      <p>{summary}</p>
    </div>
  );
};

export default BrowserPanel;
