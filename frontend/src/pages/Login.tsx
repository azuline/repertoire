import clsx from 'clsx';
import * as React from 'react';
import { useToasts } from 'react-toast-notifications';
import { AuthorizationContext } from 'src/contexts';
import { useRequestJson } from 'src/hooks';

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
      <form className="self-center mx-auto" onSubmit={onSubmit}>
        <div>
          <input
            autoFocus
            className="mr-6"
            placeholder="Authorization token"
            ref={input}
            style={inputStyle}
          />
          <button type="submit">Login</button>
        </div>
        <div className="flex items-center mt-2">
          <input className="mx-2 cursor-pointer" id="permanent" type="checkbox" ref={permanent} />
          <label className="cursor-pointer" htmlFor="permanent">
            Remember me
          </label>
        </div>
      </form>
    </div>
  );
};
