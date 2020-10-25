import * as React from 'react';
import clsx from 'clsx';
import { AuthorizationContext } from 'src/contexts';
import { gql } from 'graphql-request';
import { createGQLClient } from 'src/common';
import { useToasts } from 'react-toast-notifications';

const QUERY = gql`
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
  const { setToken, setUser } = React.useContext(AuthorizationContext);
  const { addToast, removeToast } = useToasts();

  /* This function makes a query to the backend for the currently authenticated
   * user, using the `input` as the authorization token. If it is successful,
   * we persist our token and current user information to localStorage;
   * otherwise, show the user an error.
   *
   * When token and user are set, the page automatically redirects to the
   * intended destination.
   */
  const onSubmit = React.useCallback(async () => {
    if (!input.current) return; // If we don't have an input, we cannot submit.

    const client = createGQLClient(input.current.value);

    try {
      const data = await client.request(QUERY);
      setUser(data.user);
      setToken(input.current.value);
      addToast('Successfully logged in.', { appearance: 'success' });
    } catch (data) {
      data.response.errors.forEach((e: { message: string }): void => {
        addToast(e.message, { appearance: 'error' });
      });
    }
  }, [input, setToken, setUser, addToast, removeToast]);

  return (
    <div className={clsx(className, 'flex content-center')} style={pageStyle}>
      <div className="mx-auto self-center">
        <input
          autoFocus
          className="padded mr-6"
          placeholder="Token"
          ref={input}
          style={inputStyle}
        />
        <button className="padded bg-green-400" onClick={onSubmit}>
          Login
        </button>
      </div>
    </div>
  );
};
