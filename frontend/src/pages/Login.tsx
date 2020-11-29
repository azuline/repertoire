import clsx from 'clsx';
import * as React from 'react';
import { useToasts } from 'react-toast-notifications';
import { AuthorizationContext } from 'src/contexts';
import { useRequestJson } from 'src/hooks';

const inputStyle = { maxWidth: '600px', minWidth: '300px', width: '50vw' };

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
        body: JSON.stringify({ permanent: permanent.current.value === 'on' }),
        method: 'POST',
        token: input.current.value,
      });

      if (csrfToken) {
        addToast('Successfully logged in.', { appearance: 'success' });
        setCsrf(csrfToken);
        setLoggedIn(true);
      } else {
        addToast('Invalid authorization token.', { appearance: 'error' });
      }
    },
    [input, permanent, setLoggedIn, setCsrf, addToast, requestJson],
  );

  return (
    <div className={clsx(className, 'flex content-center')}>
      <form className="self-center mx-auto" onSubmit={onSubmit}>
        <div>
          <input
            ref={input}
            autoFocus
            className="mr-6"
            placeholder="Authorization token"
            style={inputStyle}
          />
          <button type="submit">Login</button>
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
