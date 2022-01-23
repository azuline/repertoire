import * as React from 'react';
import { useHistory } from 'react-router';
import { useToasts } from 'react-toast-notifications';
import tw from 'twin.macro';

import { Button, Input } from '~/components';
import { AuthorizationContext } from '~/contexts';
import { useRequestJson } from '~/hooks';
import { Layout } from '~/layout';

export const Login: React.FC = () => {
  const input = React.useRef<HTMLInputElement>(null);
  const permanent = React.useRef<HTMLInputElement>(null);

  const history = useHistory();
  const { setLoggedIn, setCsrf } = React.useContext(AuthorizationContext);
  const requestJson = useRequestJson<{ csrfToken: string }>();
  const { addToast } = useToasts();

  const onSubmit = async (event: React.FormEvent<HTMLFormElement>): Promise<void> => {
    event.preventDefault();

    if (!input.current || !permanent.current) {
      return;
    }

    try {
      const { csrfToken } = await requestJson('/api/session', {
        body: JSON.stringify({ permanent: permanent.current.value === 'on' }),
        method: 'POST',
        token: input.current.value,
      });

      if (csrfToken) {
        addToast('Successfully logged in.', { appearance: 'success' });
        setCsrf(csrfToken);
        setLoggedIn(true);
        history.push('/');
      } else {
        throw new Error('Invalid authorization token.');
      }
    } catch {
      addToast('Login failed.', { appearance: 'error' });
    }
  };

  return (
    <Layout tw="flex content-center full items-center">
      <form tw="self-center mx-auto" onSubmit={onSubmit}>
        <div tw="flex">
          <Input
            ref={input}
            autoFocus
            id="login-token"
            name="password"
            placeholder="Authorization token"
            tw="flex-grow mr-6 max-width[600px] min-width[300px] width[50vw]"
          />
          <Button id="login-btn" type="submit">
            Login
          </Button>
        </div>
        <div
          css={[
            tw`flex items-center mt-2`,
            tw`max-width[600px] min-width[500px] width[50vw]`,
          ]}
        >
          <Input
            ref={permanent}
            id="permanent"
            tw="mx-2 cursor-pointer"
            type="checkbox"
          />
          <label htmlFor="permanent" tw="cursor-pointer">
            Remember me
          </label>
        </div>
      </form>
    </Layout>
  );
};
