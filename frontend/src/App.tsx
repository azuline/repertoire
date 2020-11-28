import clsx from 'clsx';
import * as React from 'react';
import { BrowserRouter } from 'react-router-dom';
import { Background, NowPlayingBar, Sidebar } from 'src/components';
import { AuthorizationContext, GlobalContexts, ThemeContext } from 'src/contexts';
import { Login, Routes } from 'src/pages';

const bodyStyle = { height: 'calc(100vh - 4rem)', maxHeight: 'calc(100vh - 4rem)' };

const App: React.FC = () => (
  <BrowserRouter>
    <GlobalContexts>
      <Body />
    </GlobalContexts>
  </BrowserRouter>
);

const Body: React.FC = () => {
  const { loggedIn } = React.useContext(AuthorizationContext);
  const { theme } = React.useContext(ThemeContext);

  return (
    <div className={clsx(theme, 'flex flex-col w-full h-screen app')}>
      {!loggedIn ? (
        <Login className="flex-1" />
      ) : (
        <>
          <div className="flex flex-1 w-screen" style={bodyStyle}>
            <Sidebar />
            <div className="relative flex-1 w-full min-w-0 sm:flex sm:flex-col">
              <Background />
              <Routes />
            </div>
          </div>
          <NowPlayingBar />
        </>
      )}
    </div>
  );
};

export default App;
