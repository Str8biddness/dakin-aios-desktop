import React from 'react';
import ChatPanel from './ChatPanel';
import BrowserPanel from './BrowserPanel';
import TerminalPanel from './TerminalPanel';
import ProjectDirectorPanel from './ProjectDirectorPanel';

const App: React.FC = () => {
  return (
    <div className="app">
      <ChatPanel />
      <BrowserPanel />
      <TerminalPanel />
      <ProjectDirectorPanel />
    </div>
  );
};

export default App;
