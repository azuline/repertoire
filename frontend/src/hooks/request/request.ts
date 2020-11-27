import * as React from 'react';
import { AuthorizationContext } from 'src/contexts';
import { RequestError } from 'src/types';

export type RequestT<T> = (
  url: string,
  opts?: { method?: string; token?: string; contentType?: string; body?: string },
) => Promise<T>;

/**
 * A hook that returns a function that makes a HTTP request to the backend. It automatically
 * includes the session cookie and CSRF token on non-GET requests. It also accepts a token parameter
 * for token-based authentication.
 *
 * @returns A function that makes a HTTP request to the backend.
 */
export const useRequest = (): RequestT<Response> => {
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
