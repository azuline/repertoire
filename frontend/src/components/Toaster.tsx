import * as React from 'react';
import { ToastContainer } from 'react-toastify';

export const Toaster: React.FC = () => {
  return (
    <ToastContainer
      autoClose={1500}
      closeOnClick
      hideProgressBar={true}
      limit={3}
      position="top-center"
    />
  );
};
