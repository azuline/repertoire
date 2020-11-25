import * as React from 'react';
import { ToastProvider as RawProvider } from 'react-toast-notifications';

export const ToastProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  return (
    <RawProvider
      autoDismiss
      autoDismissTimeout={1500}
      placement="top-center"
      transitionDuration={100}
    >
      {children}
    </RawProvider>
  );
};
