import * as React from 'react';
import { QueryCache, ReactQueryCacheProvider } from 'react-query';

import { AuthorizationProvider } from './Authorization';
import { BackgroundProvider } from './Background';
import { PlayQueueProvider } from './PlayQueue';
import { SidebarProvider } from './Sidebar';
import { ThemeProvider } from './Theme';
import { ToastProvider } from './Toaster';
import { VolumeProvider } from './Volume';

export * from './Authorization';
export * from './Background';
export * from './PlayQueue';
export * from './Sidebar';
export * from './Theme';
export * from './Toaster';
export * from './Volume';

export const GlobalContexts: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const queryCache = new QueryCache();

  return (
    <ToastProvider>
      <ReactQueryCacheProvider queryCache={queryCache}>
        <AuthorizationProvider>
          <PlayQueueProvider>
            <ThemeProvider>
              <VolumeProvider>
                <SidebarProvider>
                  <BackgroundProvider>{children}</BackgroundProvider>
                </SidebarProvider>
              </VolumeProvider>
            </ThemeProvider>
          </PlayQueueProvider>
        </AuthorizationProvider>
      </ReactQueryCacheProvider>
    </ToastProvider>
  );
};
