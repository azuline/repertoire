import React from 'react';
import { BrowserRouter } from 'react-router-dom';
import tw from 'twin.macro';

import { Background, FullPageLoading, NowPlayingBar, Sidebar } from '~/components';
import { AuthorizationContext, GlobalContexts, ThemeContext } from '~/contexts';
import { AuthedRoutes, UnauthedRoutes } from '~/pages';
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
  const { loggedIn, loading } = React.useContext(AuthorizationContext);
  const { theme } = React.useContext(ThemeContext);

  return (
    <div tw="w-full min-h-0 bg-background-700 text-foreground-50">
      <div className={theme} tw="flex flex-col h-screen">
        {((): React.ReactNode => {
          switch (true) {
            case loading:
              return <FullPageLoading />;
            case loggedIn:
              return <AuthedBody />;
            default:
              return <UnauthedRoutes />;
          }
        })()}
      </div>
    </div>
  );
};

const AuthedBody: React.FC = () => {
  return (
    <>
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
            <AuthedRoutes />
          </div>
        </div>
      </div>
      <NowPlayingBar />
    </>
  );
};

export default App;
