import { useCallback, useContext, useState } from 'react';

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
  const { token } = useContext(AuthenticationContext);

  const request = useCallback(
    (url, options = {}) =>
      fetch(`${apiUrl}${url}`, {
        headers: new Headers({ Authorization: `Token ${token}` }),
        ...options, // Allow options to overwrite headers.
      }),
    [token]
  );

  return request;
};
