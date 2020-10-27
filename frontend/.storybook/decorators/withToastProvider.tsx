import { ToastProvider } from 'src/contexts';
import * as React from 'react';

export const withToastProvider = (story) => {
  return <ToastProvider>{story()}</ToastProvider>;
};
