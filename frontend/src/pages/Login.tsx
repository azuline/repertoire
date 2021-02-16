import clsx from 'clsx';
import * as React from 'react';
import { useToasts } from 'react-toast-notifications';

import { Button } from '~/components';
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
    <div className={clsx(theme, 'flex content-center app h-screen w-full items-center')}>
      <form className="self-center mx-auto" onSubmit={onSubmit}>
        <div>
          <input
            ref={input}
            autoFocus
            className="mr-6"
            placeholder="Authorization token"
            style={{ maxWidth: '600px', minWidth: '300px', width: '50vw' }}
          />
          <Button type="submit">Login</Button>
        </div>
        <div className="flex items-center mt-2">
          <input ref={permanent} className="mx-2 cursor-pointer" id="permanent" type="checkbox" />
          <label className="cursor-pointer" htmlFor="permanent">
            Remember me
          </label>
        </div>
      </form>
    </div>
  );
};
