import * as React from 'react';
import { useRequest, Request } from './request';

export const useRequestBlob = (): Request<Blob> => {
  const request = useRequest();

  const requestBlob = React.useCallback(
    async (url, opts = {}) => {
      const response = await request(url, { ...opts, contentType: 'application/octet-stream' });
      return await response.blob();
    },
    [request],
  );

  return requestBlob;
};
