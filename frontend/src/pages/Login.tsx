import * as React from 'react';
import clsx from 'clsx';
import { AuthorizationContext } from 'src/contexts';
import { useToasts } from 'react-toast-notifications';
import { useRawGQLQuery } from 'src/hooks';
import { UserT } from 'src/types';

const QUERY = `
  query {
    user {
      id
			username
    }
  }
`;

const pageStyle = { maxHeight: 'calc(100vh - 120px)' };
const inputStyle = { width: '50vw', minWidth: '300px', maxWidth: '600px' };

export const Login: React.FC<{ className?: string }> = ({ className = '' }) => {
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
    <div className={clsx(className, 'flex content-center')} style={pageStyle}>
      <form className="mx-auto self-center" onSubmit={onSubmit}>
        <input autoFocus className="mr-6" placeholder="Token" ref={input} style={inputStyle} />
        <button type="submit" className="bg-green-400">
          Login
        </button>
      </form>
    </div>
  );
};
