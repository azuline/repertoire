import * as React from 'react';

import { AuthorizationProvider } from './Authorization';
import { ToastProvider } from './Toaster';

export * from './Authorization';
export * from './Toaster';

type GCProps = { children: React.ReactNode };

export const GlobalContexts: React.FC<GCProps> = ({ children }) => {
  return (
    <ToastProvider>
      <AuthorizationProvider>{children}</AuthorizationProvider>
    </ToastProvider>
  );
};
