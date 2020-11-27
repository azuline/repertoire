import clsx from 'clsx';
import * as React from 'react';
import { BrowserRouter } from 'react-router-dom';
import { NowPlayingBar, Sidebar } from 'src/components';
import { AuthorizationContext, GlobalContexts, SidebarContext, ThemeContext } from 'src/contexts';
import { Login } from 'src/pages';
import { Routes } from 'src/Routes';

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
  const { isSidebarOpen } = React.useContext(SidebarContext);
  const { theme } = React.useContext(ThemeContext);

  return (
    <div className={clsx(theme, 'flex flex-col w-full h-screen app')}>
      {!loggedIn ? (
        <Login className="flex-1" />
      ) : (
        <>
          <div className="flex flex-1" style={bodyStyle}>
            <Sidebar />
            <div
              className={clsx(isSidebarOpen && 'hidden sm:flex sm:flex-col')}
              style={{ width: isSidebarOpen ? 'calc(100% - 14rem)' : '100%' }}
            >
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
