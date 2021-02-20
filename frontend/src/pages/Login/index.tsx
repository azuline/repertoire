import * as React from 'react';
import { useToasts } from 'react-toast-notifications';

import { Button, Input } from '~/components';
import { AuthorizationContext, ThemeContext } from '~/contexts';
import { useRequestJson } from '~/hooks';

export const Login: React.FC = () => {
  const input = React.useRef<HTMLInputElement>(null);
  const permanent = React.useRef<HTMLInputElement>(null);
  const { setLoggedIn, setCsrf } = React.useContext(AuthorizationContext);
  const requestJson = useRequestJson<{ csrfToken: string }>();
  const { addToast } = useToasts();
  const { theme } = React.useContext(ThemeContext);

  const onSubmit = async (event: React.FormEvent<HTMLFormElement>): Promise<void> => {
    event.preventDefault();

    if (!input.current || !permanent.current) return;

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
      } else {
        throw new Error('Invalid authorization token.');
      }
    } catch {
      addToast('Login failed.', { appearance: 'error' });
    }
  };

  return (
    <div className={theme}>
      <div tw="flex content-center h-screen w-full items-center">
        <form tw="self-center mx-auto" onSubmit={onSubmit}>
          <div>
            <Input
              ref={input}
              autoFocus
              placeholder="Authorization token"
              tw="mr-6 max-width[600px] min-width[300px] width[50vw]"
            />
            <Button type="submit">Login</Button>
          </div>
          <div tw="flex items-center mt-2">
            <Input ref={permanent} id="permanent" tw="mx-2 cursor-pointer" type="checkbox" />
            <label htmlFor="permanent" tw="cursor-pointer">
              Remember me
            </label>
          </div>
        </form>
      </div>
    </div>
  );
};
