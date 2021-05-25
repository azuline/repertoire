import * as React from 'react';
import { Route, Switch } from 'react-router-dom';

import { FullPageLoading } from '~/components';
import { useHasFirstUser } from '~/hooks';
import { Login, Register, UnauthenticatedError } from '~/pages';

export const UnauthedRoutes: React.FC = () => {
  const { hasFirstUser, loading, error, refetch } = useHasFirstUser();

  switch (true) {
    case loading:
      return <FullPageLoading />;
    case error:
      return (
        <UnauthenticatedError title="Unable to reach server. Please try again later" />
      );
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
