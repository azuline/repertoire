import * as React from 'react';

import { Input } from '~/components';
import { useHasFirstUser } from '~/hooks';

export const Register: React.FC = () => {
  const hasFirstUser = useHasFirstUser();

  return (
    <div tw="flex flex-col w-full">
      {!hasFirstUser && (
        <div>ok ur the first user so register as admin write proper message later</div>
      )}
      <div tw="my-8 text-center">hello</div>
      {hasFirstUser && (
        <>
          give the invite code here because you arent first user
          <Input />
        </>
      )}
    </div>
  );
};
