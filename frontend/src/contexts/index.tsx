import * as React from 'react';

import { QueryCache, ReactQueryCacheProvider } from 'react-query';

import { AuthorizationProvider } from './Authorization';
import { ToastProvider } from './Toaster';
import { TitleProvider } from './Title';

export * from './Authorization';
export * from './Toaster';
export * from './Title';

export const GlobalContexts: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const queryCache = new QueryCache();

  return (
    <AuthorizationProvider>
      <ToastProvider>
        <TitleProvider>
          <ReactQueryCacheProvider queryCache={queryCache}>{children}</ReactQueryCacheProvider>
        </TitleProvider>
      </ToastProvider>
    </AuthorizationProvider>
  );
};
