import React from 'react';
import { useHistory } from 'react-router';

import { Button } from '~/components';

type ISuccess = {
  nickname: string;
  token: string;
  onSuccess?: () => void;
};

export const Success: React.FC<ISuccess> = ({ nickname, token, onSuccess }) => {
  const history = useHistory();

  const onClick = (): void => {
    if (onSuccess) {
      onSuccess();
    }

    history.push('/login');
  };

  return (
    <div tw="relative flex flex-col space-y-4 justify-center full items-center">
      <div>Hi {nickname}, thanks for registering! Your authorization token is:</div>
      <pre tw="text-primary-400">{token}</pre>
      <div>
        Record this authorization token in a safe place. You will need it to log in.
      </div>
      <Button type="button" onClick={onClick}>
        Log in
      </Button>
    </div>
  );
};
