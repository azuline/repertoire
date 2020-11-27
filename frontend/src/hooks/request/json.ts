import * as React from 'react';

import { RequestT, useRequest } from './request';

/**
 * A wrapper around the ``request`` hook. This hook returns a function that make a HTTP request
 * and parses the resulting JSON.
 *
 * @returns A requestJson function.
 */
export const useRequestJson = <T>(): RequestT<T> => {
  const request = useRequest();

  const requestJson = React.useCallback(
    async (url, opts = {}) => {
      const response = await request(url, { ...opts, contentType: 'application/json' });
      return response.json();
    },
    [request],
  );

  return requestJson;
};
