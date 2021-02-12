import clsx from 'clsx';
import * as React from 'react';
import { BrowserRouter } from 'react-router-dom';
import { Background, NowPlayingBar, Sidebar } from '~/components';
import { AuthorizationContext, GlobalContexts, ThemeContext } from '~/contexts';
import { Login, Routes } from '~/pages';

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

  if (!loggedIn) return <Login />;

  return (
    <div className={clsx(theme, 'w-full min-h-0 flex flex-col h-screen app')}>
      <div
        className="flex flex-1 w-full"
        style={{ height: 'calc(100% - 4rem)', minHeight: 'calc(100% - 4rem)' }}
      >
        <Sidebar />
        <div className="relative flex flex-col min-w-0 full">
          <Background />
          <div className="relative flex flex-col min-h-0 px-6 overflow-y-auto md:px-8 full">
            <Routes />
          </div>
        </div>
      </div>
      <NowPlayingBar />
    </div>
  );
};

export default App;
