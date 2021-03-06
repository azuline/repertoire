import * as React from 'react';
import { useToasts } from 'react-toast-notifications';

import { Button, Icon, Input } from '~/components';
import { useRequestJson } from '~/hooks';

import { Success } from './Success';

type IRegister = React.FC<{
  isFirstRegistration: boolean;
  inviteCode?: string;
  onSuccess?: () => void;
}>;

export const RegisterForm: IRegister = ({
  inviteCode,
  isFirstRegistration,
  onSuccess,
}) => {
  const requestJson = useRequestJson<{ token: string }>();
  const { addToast } = useToasts();

  const [nickname, setNickname] = React.useState<string>('');
  const [newToken, setNewToken] = React.useState<string | undefined>(undefined);

  const onSubmit = async (event: React.FormEvent<HTMLFormElement>): Promise<void> => {
    event.preventDefault();

    try {
      const { token } = await requestJson('/api/register', {
        body: JSON.stringify({ inviteCode, nickname }),
        method: 'POST',
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

  if (newToken !== undefined) {
    return <Success nickname={nickname} token={newToken} onSuccess={onSuccess} />;
  }

  // At the moment, this only supports the initial admin registration. Soon, we will
  // support registration by invite.
  return (
    <div tw="relative flex content-center full items-center">
      <div tw="absolute top-0 left-0 w-full h-1/2 flex items-end">
        <div tw="h-1/2 pb-28 w-full flex flex-col items-center justify-center">
          <Icon icon="logo" tw="w-32 text-primary-500 pb-8" />
          {isFirstRegistration ? (
            <>
              <div>Welcome to your new instance of repertoire!</div>
              <div>Register your admin account below!</div>
            </>
          ) : (
            <>
              <div>Welcome to repertoire!</div>
              <div>Register your new account below!</div>
            </>
          )}
        </div>
      </div>
      <form tw="z-10 self-center mx-auto" onSubmit={onSubmit}>
        <div>
          <Input
            autoFocus
            placeholder="Nickname"
            tw="mr-6 max-width[400px] min-width[200px] width[50vw]"
            value={nickname}
            onChange={(e): void => setNickname(e.target.value)}
          />
          <Button type="submit">Register</Button>
        </div>
      </form>
    </div>
  );
};
