import * as React from 'react';
import { AuthorizationContext } from 'src/contexts';
import { RequestError } from 'src/types';

export type Request<T> = (
  url: string,
  opts?: { method?: string; token?: string; contentType?: string; body?: string },
) => Promise<T>;

export const useRequest = (): Request<Response> => {
  const { loggedIn, setLoggedIn, csrf } = React.useContext(AuthorizationContext);

  const request = React.useCallback(
    async (url, { method, token, contentType, body } = {}) => {
      const response = await fetch(url, {
        credentials: 'same-origin',
        method,
        body,
        headers: new Headers({
          Authorization: token && `Token ${token}`,
          'X-CSRF-Token': method !== undefined && method !== 'GET' && csrf ? csrf : '',
          'Content-Type': contentType,
        }),
      });

      if (response.status === 401) {
        setLoggedIn(false);
        throw new RequestError('Failed to authenticate.');
      }

      return response;
    },
    [loggedIn, setLoggedIn, csrf],
  );

  return request;
};
