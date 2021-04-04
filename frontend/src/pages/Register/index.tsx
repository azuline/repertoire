import * as React from 'react';
import { useToasts } from 'react-toast-notifications';

import { Button, Icon, Input } from '~/components';
import { useRequestJson } from '~/hooks';

import { Success } from './Success';

export const Register: React.FC = () => {
  const input = React.useRef<HTMLInputElement>(null);
  const requestJson = useRequestJson<{ token: string }>();
  const { addToast } = useToasts();

  const [newToken, setNewToken] = React.useState<string | undefined>(undefined);

  const onSubmit = async (event: React.FormEvent<HTMLFormElement>): Promise<void> => {
    event.preventDefault();

    if (!input.current) {
      return;
    }

    try {
      const { token } = await requestJson('/api/register', {
        body: JSON.stringify({ nickname: input.current.value }),
        method: 'POST',
        token: input.current.value,
      });

      if (token) {
        setNewToken(token);
      } else {
        throw new Error('Registration failed.');
      }
    } catch {
      addToast('Registration failed.', { appearance: 'error' });
    }
  };

  if (input.current !== null && newToken !== undefined) {
    return <Success nickname={input.current.value} token={newToken} />;
  }

  // At the moment, this only supports the initial admin registration. Soon, we will
  // support registration by invite.
  return (
    <div tw="relative flex content-center full items-center">
      <div tw="absolute top-0 left-0 w-full h-1/2 flex items-end">
        <div tw="h-1/2 pb-28 w-full flex flex-col items-center justify-center">
          <Icon icon="logo" tw="w-32 text-primary-500 pb-8" />
          <div>Welcome to your new instance of repertoire!</div>
          <div>Register your admin account below!</div>
        </div>
      </div>
      <form tw="z-10 self-center mx-auto" onSubmit={onSubmit}>
        <div>
          <Input
            ref={input}
            autoFocus
            placeholder="Nickname"
            tw="mr-6 max-width[400px] min-width[200px] width[50vw]"
          />
          <Button type="submit">Register</Button>
        </div>
      </form>
    </div>
  );
};
