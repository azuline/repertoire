import * as React from 'react';

import { QueryCache, ReactQueryCacheProvider } from 'react-query';

import { AuthorizationProvider } from './Authorization';
import { PlayQueueProvider } from './PlayQueue';
import { SidebarProvider } from './Sidebar';
import { ThemeProvider } from './Theme';
import { ToastProvider } from './Toaster';

export * from './Authorization';
export * from './Toaster';
export * from './Sidebar';
export * from './Theme';
export * from './PlayQueue';

export const GlobalContexts: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const queryCache = new QueryCache();

  return (
    <ToastProvider>
      <ReactQueryCacheProvider queryCache={queryCache}>
        <AuthorizationProvider>
          <PlayQueueProvider>
            <ThemeProvider>
              <SidebarProvider>{children}</SidebarProvider>
            </ThemeProvider>
          </PlayQueueProvider>
        </AuthorizationProvider>
      </ReactQueryCacheProvider>
    </ToastProvider>
  );
};
