import * as React from 'react';
import clsx from 'clsx';

import { GlobalContexts, SidebarContext, ThemeContext } from 'src/contexts';

import { AuthorizationContext } from 'src/contexts';
import { BrowserRouter } from 'react-router-dom';
import { Footer } from 'src/components/Footer';
import { Login } from 'src/pages';
import { Routes } from 'src/Routes';
import { Sidebar } from 'src/components/Sidebar';

const App: React.FC = () => {
  return (
    <BrowserRouter>
      <GlobalContexts>
        <Body />
      </GlobalContexts>
    </BrowserRouter>
  );
};

const Body: React.FC = () => {
  const { loggedIn } = React.useContext(AuthorizationContext);
  const { isSidebarOpen } = React.useContext(SidebarContext);
  const { theme } = React.useContext(ThemeContext);

  return (
    <div className={clsx(theme, 'app w-full h-screen flex flex-col')}>
      {!loggedIn ? (
        <Login className="flex-1" />
      ) : (
        <>
          <div
            className="flex-1 flex"
            style={{ height: 'calc(100vh - 4rem)', maxHeight: 'calc(100vh - 4rem)' }}
          >
            <Sidebar />
            <div
              className={clsx(isSidebarOpen && 'hidden sm:flex sm:flex-col')}
              style={{ width: isSidebarOpen ? 'calc(100% - 14rem)' : '100%' }}
            >
              <Routes />
            </div>
          </div>
          <Footer />
        </>
      )}
    </div>
  );
};

export default App;
