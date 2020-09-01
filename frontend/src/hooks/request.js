import { useCallback, useContext } from 'react';

import { AuthenticationContext } from 'contexts';
import { TopToaster } from 'components/Toaster';

const apiUrl = process.env.NODE_ENV === 'development' ? 'http://localhost:5000' : '';

export const useRequest = () => {
  const { token, setToken } = useContext(AuthenticationContext);

  const toastToFailure = useCallback(() => {
    const existingToasts = TopToaster.getToasts();

    // Don't create a duplicate fail to authenticate toast.
    if (existingToasts.some(({ className }) => className === 'ToastAuthFailure')) {
      return;
    }

    TopToaster.show({
      className: 'ToastAuthFailure',
      icon: 'user',
      intent: 'danger',
      message: 'Failed to authenticate!',
      timeout: 2000,
    });
  }, []);

  const request = useCallback(
    async (url, options = {}) => {
      const response = await fetch(`${apiUrl}${url}`, {
        headers: new Headers({ Authorization: `Token ${token}` }),
        ...options, // Allow options to overwrite headers.
      });
      if (response.status === 401) {
        toastToFailure();
        setToken('');
      }
      return response;
    },
    [token, setToken, toastToFailure]
  );

  return request;
};
