import 'twin.macro';

import clsx from 'clsx';
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

  if (!loggedIn) return <Login />;

  return (
    <div
      className={clsx(theme, 'app')}
      tw="w-full min-h-0 flex flex-col h-screen bg-background-700 text-foreground"
    >
      <div
        style={{ height: 'calc(100% - 4rem)', minHeight: 'calc(100% - 4rem)' }}
        tw="flex flex-1 w-full"
      >
        <Sidebar />
        <div tw="relative flex flex-col min-w-0 w-full h-full">
          <Background />
          <div tw="relative flex flex-col min-h-0 px-6 overflow-y-auto md:px-8 w-full h-full">
            <Routes />
          </div>
        </div>
      </div>
      <NowPlayingBar />
    </div>
  );
};

export default App;
