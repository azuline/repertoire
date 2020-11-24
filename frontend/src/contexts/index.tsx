import * as React from 'react';

import { QueryCache, ReactQueryCacheProvider } from 'react-query';

import { AuthorizationProvider } from './Authorization';
import { SidebarProvider } from './Sidebar';
import { ToastProvider } from './Toaster';
import { ThemeProvider } from './Theme';

export * from './Authorization';
export * from './Toaster';
export * from './Sidebar';
export * from './Theme';

export const GlobalContexts: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const queryCache = new QueryCache();

  return (
    <ToastProvider>
      <ReactQueryCacheProvider queryCache={queryCache}>
        <AuthorizationProvider>
          <ThemeProvider>
            <SidebarProvider>{children}</SidebarProvider>
          </ThemeProvider>
        </AuthorizationProvider>
      </ReactQueryCacheProvider>
    </ToastProvider>
  );
};
