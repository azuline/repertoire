import clsx from 'clsx';
import * as React from 'react';
import { BrowserRouter } from 'react-router-dom';
import { Background, NowPlayingBar, Sidebar } from 'src/components';
import { AuthorizationContext, GlobalContexts, ThemeContext } from 'src/contexts';
import { Login, Routes } from 'src/pages';

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
    <div className={clsx(theme, 'w-full min-h-screen app')}>
      <div className="flex w-full pb-16">
        <Sidebar />
        <div className="relative w-full min-w-0">
          <Background />
          <div className="z-10 flex-1 full">
            <Routes />
          </div>
        </div>
      </div>
      <NowPlayingBar />
    </div>
  );
};

export default App;
