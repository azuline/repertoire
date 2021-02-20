import * as React from 'react';
import { BrowserRouter } from 'react-router-dom';
import tw from 'twin.macro';

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
          <div
            css={[
              tw`w-full height[calc(100% - 4rem)] min-height[calc(100% - 4rem)]`,
              tw`flex flex-1`,
            ]}
          >
            <Sidebar />
            <div tw="full relative flex flex-col min-w-0">
              <Background />
              <div
                css={[
                  tw`full px-6 md:px-8`,
                  tw`relative flex flex-col min-h-0 overflow-y-auto`,
                ]}
              >
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
