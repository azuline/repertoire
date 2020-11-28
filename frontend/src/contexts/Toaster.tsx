import * as React from 'react';
import { ToastProvider as RawProvider } from 'react-toast-notifications';

export const ToastProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => (
  <RawProvider
    autoDismiss
    autoDismissTimeout={4000}
    placement="top-center"
    transitionDuration={100}
  >
    {children}
  </RawProvider>
);
