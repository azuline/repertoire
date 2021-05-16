import React from 'react';

import { AuthorizationProvider } from './Authorization';
import { BackgroundProvider } from './Background';
import { GraphQLProvider } from './GraphQL';
import { PlayQueueProvider } from './PlayQueue';
import { ThemeProvider } from './Theme';
import { ToastProvider } from './Toaster';
import { VolumeProvider } from './Volume';

export * from './Authorization';
export * from './Background';
export * from './PlayQueue';
export * from './Theme';
export * from './Toaster';
export * from './Volume';

type IGlobalContexts = React.FC<{ children: React.ReactNode }>;

export const GlobalContexts: IGlobalContexts = ({ children }) => (
  <ToastProvider>
    <AuthorizationProvider>
      <GraphQLProvider>
        <PlayQueueProvider>
          <ThemeProvider>
            <VolumeProvider>
              <BackgroundProvider>{children}</BackgroundProvider>
            </VolumeProvider>
          </ThemeProvider>
        </PlayQueueProvider>
      </GraphQLProvider>
    </AuthorizationProvider>
  </ToastProvider>
);
