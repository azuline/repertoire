import * as React from 'react';

import { AuthorizationProvider } from './Authorization';

export * from './Authorization';

type GCProps = { children: React.ReactNode };

export const GlobalContexts: React.FC<GCProps> = ({ children }) => {
  return <AuthorizationProvider>{children}</AuthorizationProvider>;
};
