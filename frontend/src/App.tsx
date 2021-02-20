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
    <div tw="w-full min-h-0 bg-background-700 text-foreground">
      {loggedIn ? (
        <div className={theme} tw="flex flex-col h-screen">
          <div tw="flex flex-1 w-full height[calc(100% - 4rem)] min-height[calc(100% - 4rem)]">
            <Sidebar />
            <div tw="relative flex flex-col min-w-0 full">
              <Background />
              <div tw="relative flex flex-col min-h-0 px-6 overflow-y-auto md:px-8 full">
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
