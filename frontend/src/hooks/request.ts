import * as React from 'react';

import { AuthorizationContext } from 'src/contexts';
import { RequestError } from 'src/types';
import { useToasts } from 'react-toast-notifications';

type Request<T> = (
  url: string,
  { token }?: { method?: string | undefined; token?: string | undefined },
) => Promise<T>;

export const useRequest = (): Request<Response> => {
  const { loggedIn, setLoggedIn } = React.useContext(AuthorizationContext);
  const { addToast } = useToasts();

  const request = React.useCallback(
    async (url, { method, token } = {}) => {
      if (!loggedIn && !token) {
        throw new RequestError('Not logged in.');
      }

      const response = await fetch(url, {
        credentials: 'same-origin',
        method: method,
        headers: token ? new Headers({ Authorization: `Token ${token}` }) : undefined,
      });

      if (response.status === 401) {
        addToast('Failed to authenticate.', { appearance: 'error' });
        setLoggedIn(false);
        throw new RequestError('Failed to authenticate.');
      }

      return response;
    },
    [loggedIn, setLoggedIn, addToast],
  );

  return request;
};

export const useRequestBlob = (): Request<Blob> => {
  const request = useRequest();

  const requestBlob = React.useCallback(
    async (url, opts) => {
      const response = await request(url, opts);
      return await response.blob();
    },
    [request],
  );

  return requestBlob;
};

export const useRequestJson = <T>(): Request<T> => {
  const request = useRequest();

  const requestBlob = React.useCallback(
    async (url, opts) => {
      const response = await request(url, opts);
      return await response.json();
    },
    [request],
  );

  return requestBlob;
};
