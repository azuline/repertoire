import * as React from 'react';
import { BrowserRouter } from 'react-router-dom';

import { Background, FullPageLoading, Header, NowPlayingBar } from '~/components';
import { AuthorizationContext, GlobalContexts, ThemeContext } from '~/contexts';
import { AuthedRoutes, UnauthedRoutes } from '~/routes';
import { AppStyles } from '~/Styles';

export const App: React.FC = () => (
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
    <div tw="w-full bg-background-900 text-foreground-50 min-width[400px]">
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
      <Header />
      <div tw="full flex min-h-0">
        <div tw="full relative min-w-0">
          <Background />
          <AuthedRoutes />
        </div>
      </div>
      <NowPlayingBar />
    </>
  );
};
