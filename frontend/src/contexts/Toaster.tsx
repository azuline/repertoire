import React from 'react';
import { ToastProvider as RawProvider } from 'react-toast-notifications';
import tw, { styled } from 'twin.macro';

type IProvider = React.FC<{ children: React.ReactNode }>;

export const ToastProvider: IProvider = ({ children }) => (
  <Toaster>
    <RawProvider
      autoDismiss
      autoDismissTimeout={4000}
      placement="top-center"
      transitionDuration={100}
    >
      {children}
    </RawProvider>
  </Toaster>
);

const Toaster = styled.div`
  .react-toast-notifications__toast__content,
  .react-toast-notifications__toast__dismiss-button,
  .react-toast-notifications__toast__icon-wrapper {
    ${tw`flex items-center`}
  }
  .react-toast-notifications__toast__icon-wrapper {
    ${tw`justify-center`}
  }
`;
