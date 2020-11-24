import * as React from 'react';

import { AuthorizationContext } from 'src/contexts';
import clsx from 'clsx';
import { useRequestJson } from 'src/hooks';
import { useToasts } from 'react-toast-notifications';

const inputStyle = { width: '50vw', minWidth: '300px', maxWidth: '600px' };

export const Login: React.FC<{ className?: string }> = ({ className }) => {
  const input = React.useRef<HTMLInputElement>(null);
  const permanent = React.useRef<HTMLInputElement>(null);
  const { setLoggedIn, setCsrf } = React.useContext(AuthorizationContext);
  const requestJson = useRequestJson<{ csrfToken: string }>();
  const { addToast } = useToasts();

  const onSubmit = React.useCallback(
    async (event) => {
      event.preventDefault();

      if (!input.current || !permanent.current) return;

      const { csrfToken } = await requestJson('/session', {
        method: 'POST',
        token: input.current.value,
        body: JSON.stringify({ permanent: permanent.current.value === 'on' }),
      });

      if (csrfToken) {
        addToast('Successfully logged in.', { appearance: 'success' });
        setCsrf(csrfToken);
        setLoggedIn(true);
      } else {
        addToast('Invalid authorization token.', { appearance: 'error' });
      }
    },
    [input, permanent, setLoggedIn, setCsrf, addToast],
  );

  return (
    <div className={clsx(className, 'flex content-center')}>
      <form className="mx-auto self-center" onSubmit={onSubmit}>
        <div>
          <input
            autoFocus
            className="mr-6"
            placeholder="Authorization token"
            ref={input}
            style={inputStyle}
          />
          <button type="submit" className="px-4 py-2 bg-primary hover:bg-primary">
            Login
          </button>
        </div>
        <div className="mt-2 flex items-center">
          <input className="mx-2 cursor-pointer" id="permanent" type="checkbox" ref={permanent} />
          <label className="cursor-pointer" htmlFor="permanent">
            Remember me
          </label>
        </div>
      </form>
    </div>
  );
};
