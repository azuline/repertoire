import * as React from 'react';

import { QueryCache, ReactQueryCacheProvider } from 'react-query';

import { AuthorizationProvider } from './Authorization';
import { SidebarProvider } from './Sidebar';
import { ToastProvider } from './Toaster';

export * from './Authorization';
export * from './Toaster';
export * from './Sidebar';

export const GlobalContexts: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const queryCache = new QueryCache();

  return (
    <AuthorizationProvider>
      <ToastProvider>
        <ReactQueryCacheProvider queryCache={queryCache}>
          <SidebarProvider>{children}</SidebarProvider>
        </ReactQueryCacheProvider>
      </ToastProvider>
    </AuthorizationProvider>
  );
};
