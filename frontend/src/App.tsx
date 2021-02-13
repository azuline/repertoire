import 'twin.macro';

import * as React from 'react';
import { BrowserRouter } from 'react-router-dom';

import { Background, NowPlayingBar, Sidebar } from '~/components';
import { AuthorizationContext, GlobalContexts, ThemeContext } from '~/contexts';
import { Login, Routes } from '~/pages';
import { AppStyles } from '~/Styles';

const App: React.FC = () => (
  <BrowserRouter>
    <GlobalContexts>
      <AppStyles>
        <Body />
      </AppStyles>
    </GlobalContexts>
  </BrowserRouter>
);

const Body: React.FC = () => {
  const { loggedIn } = React.useContext(AuthorizationContext);
  const { theme } = React.useContext(ThemeContext);

  return (
    <div tw="w-full min-h-0 flex flex-col h-screen bg-background-700 text-foreground">
      {loggedIn ? (
        <div className={theme}>
          <div
            style={{ height: 'calc(100% - 4rem)', minHeight: 'calc(100% - 4rem)' }}
            tw="flex flex-1 w-full"
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
      ) : (
        <Login />
      )}
    </div>
  );
};

export default App;
