import * as React from 'react';

import { AuthorizationContext } from '~/contexts';

export type IRequest<T> = (
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
export const useRequest = (): IRequest<Response> => {
  const { setLoggedIn, csrf } = React.useContext(AuthorizationContext);

  const request: IRequest<Response> = async (url, { method, token, contentType, body } = {}) => {
    const headers = new Headers();

    headers.set('Authorization', token ? `Token ${token}` : '');
    headers.set('Content-Type', contentType ?? '');
    headers.set('X-CSRF-Token', method !== undefined && method !== 'GET' && csrf ? csrf : '');

    const response = await fetch(url, { body, credentials: 'same-origin', headers, method });

    if (response.status === 401) {
      setLoggedIn(false);
      throw new Error('Failed to authenticate.');
    }

    return response;
  };

  return request;
};

/**
 * A wrapper around the ``request`` hook. This hook returns a function that make a HTTP request
 * and parses the resulting JSON.
 *
 * @returns A requestJson function.
 */
export const useRequestJson = <T>(): IRequest<T> => {
  const request = useRequest();

  const requestJson: IRequest<T> = async (url, opts = {}) => {
    const response = await request(url, { ...opts, contentType: 'application/json' });
    return response.json();
  };

  return requestJson;
};
