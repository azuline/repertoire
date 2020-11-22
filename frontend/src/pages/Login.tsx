import * as React from 'react';

import { AuthorizationContext } from 'src/contexts';
import { UserT } from 'src/types';
import clsx from 'clsx';
import { useRawGQLQuery } from 'src/hooks';
import { useToasts } from 'react-toast-notifications';

const QUERY = `
  query {
    user {
      id
			username
    }
  }
`;

const inputStyle = { width: '50vw', minWidth: '300px', maxWidth: '600px' };

export const Login: React.FC<{ className?: string | undefined }> = ({ className }) => {
  const input = React.useRef<HTMLInputElement>(null);
  const { setToken } = React.useContext(AuthorizationContext);
  const gqlQuery = useRawGQLQuery<UserT>();
  const { addToast } = useToasts();

  const onSubmit = React.useCallback(
    async (event) => {
      event.preventDefault();

      if (!input.current) return;

      try {
        await gqlQuery(QUERY, { authorization: input.current.value });
        setToken(input.current.value);
        addToast('Successfully logged in.', { appearance: 'success' });
      } catch (errors) {
        addToast('Invalid authorization token.', { appearance: 'error' });
      }
    },
    [input, gqlQuery, setToken, addToast],
  );

  return (
    <div className={clsx(className, 'flex content-center')}>
      <form className="mx-auto self-center" onSubmit={onSubmit}>
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
      </form>
    </div>
  );
};
