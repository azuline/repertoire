import * as React from 'react';

import { AuthorizationContext } from '~/contexts';
import { RequestError } from '~/types';

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
  const { setLoggedIn, csrf } = React.useContext(AuthorizationContext);

  const request: RequestT<Response> = async (url, { method, token, contentType, body } = {}) => {
    const headers = new Headers();

    headers.set('Authorization', token ? `Token ${token}` : '');
    headers.set('Content-Type', contentType ?? '');
    headers.set('X-CSRF-Token', method !== undefined && method !== 'GET' && csrf ? csrf : '');

    const response = await fetch(url, { body, credentials: 'same-origin', headers, method });

    if (response.status === 401) {
      setLoggedIn(false);
      throw new RequestError('Failed to authenticate.');
    }

    return response;
  };

  return request;
};
