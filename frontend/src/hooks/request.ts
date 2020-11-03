import * as React from 'react';

import { AuthorizationContext } from 'src/contexts';
import { useToasts } from 'react-toast-notifications';

import { API_URL } from 'src/constants';
import { RequestError } from 'src/types';

type Request<T> = (url: string) => Promise<T>;

export const useRequest = (): Request<Response> => {
  const { token, setToken } = React.useContext(AuthorizationContext);
  const { addToast } = useToasts();

  const request = React.useCallback(
    async (url) => {
      if (!token) {
        throw new RequestError('Failed to authenticate.');
      }

      const response = await fetch(`${API_URL}${url}`, {
        headers: new Headers({ Authorization: `Token ${token}` }),
      });

      if (response.status === 401) {
        addToast('Invalid authorization token.', { appearance: 'error' });
        setToken(null);
        throw new RequestError('Failed to authenticate.');
      }

      return response;
    },
    [token, setToken, addToast],
  );

  return request;
};

export const useRequestBlob = (): Request<Blob> => {
  const request = useRequest();

  const requestBlob = React.useCallback(
    async (url) => {
      const response = await request(url);
      return await response.blob();
    },
    [request],
  );

  return requestBlob;
};
