import * as React from 'react';

import { useHasFirstUser } from '~/hooks';

export const Register: React.FC = () => {
  const inviteOnly = useHasFirstUser();

  return (
    <div tw="flex flex-col w-full">
      <div tw="my-8 text-center">hello</div>
    </div>
  );
};
