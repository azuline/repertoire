import * as React from 'react';

import { AuthorizationProvider } from './Authorization';
import { ToastProvider } from './Toaster';
import { QueryCache, ReactQueryCacheProvider } from 'react-query';

export * from './Authorization';
export * from './Toaster';
export * from './Pagination';

type GCProps = { children: React.ReactNode };

export const GlobalContexts: React.FC<GCProps> = ({ children }) => {
  const queryCache = new QueryCache();

  return (
    <AuthorizationProvider>
      <ToastProvider>
        <ReactQueryCacheProvider queryCache={queryCache}>
          {children}
        </ReactQueryCacheProvider>
      </ToastProvider>
    </AuthorizationProvider>
  );
};
