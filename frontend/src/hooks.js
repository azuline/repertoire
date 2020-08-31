import { useCallback, useContext, useState } from 'react';
import { TopToaster } from 'components/Toaster';

import { AuthenticationContext } from 'contexts';

export const usePersistentState = (localStorageKey, defaultValue) => {
  const [value, setValue] = useState(() => {
    const storedValue = localStorage.getItem(localStorageKey);
    return storedValue ? JSON.parse(storedValue) : defaultValue;
  });

  const setPersistentValue = useCallback(
    (newValue, persist = true) => {
      setValue((value) => {
        const toStore = newValue instanceof Function ? newValue(value) : newValue;
        if (persist) {
          localStorage.setItem(localStorageKey, JSON.stringify(toStore));
        }
        return toStore;
      });
    },
    [setValue, localStorageKey]
  );

  return [value, setPersistentValue];
};

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
