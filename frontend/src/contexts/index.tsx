import * as React from 'react';

import { QueryCache, ReactQueryCacheProvider } from 'react-query';

import { AuthorizationProvider } from './Authorization';
import { ToastProvider } from './Toaster';

export * from './Authorization';
export * from './Toaster';

export const GlobalContexts: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const queryCache = new QueryCache();

  return (
    <AuthorizationProvider>
      <ToastProvider>
        <ReactQueryCacheProvider queryCache={queryCache}>{children}</ReactQueryCacheProvider>
      </ToastProvider>
    </AuthorizationProvider>
  );
};
