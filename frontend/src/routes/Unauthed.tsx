import * as React from 'react';
import { Route, Switch } from 'react-router-dom';

import { FullPageLoading } from '~/components';
import { useHasFirstUser } from '~/hooks';
import { ErrorPage, Login, Register } from '~/pages';

export const UnauthedRoutes: React.FC = () => {
  const { hasFirstUser, loading, error, refetch } = useHasFirstUser();

  switch (true) {
    case loading:
      return <FullPageLoading />;
    case error:
      return <ErrorPage title="Unable to reach server. Please try again later" />;
    case !hasFirstUser:
      return <Register isFirstRegistration onSuccess={refetch} />;
    default:
      return (
        <Switch>
          <Route component={Register} path="/register/:code" />
          <Route component={Register} path="/register" />
          <Route component={Login} path="/login" />
          <Route component={Login} path="/" />
        </Switch>
      );
  }
};
