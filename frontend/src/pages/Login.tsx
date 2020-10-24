import * as React from 'react';
import clsx from 'clsx';
import { AuthorizationContext } from 'contexts';

// const USER_QUERY = `
//   query {
//     user {
//       __typename

//       ... on User {
//         id
//         username
//       }

//       ... on Error {
//         error
//         message
//       }
//     }
//   }
// `;

const pageStyle = { maxHeight: 'calc(100vh - 120px)' };
const inputStyle = { width: '50vw', minWidth: '300px', maxWidth: '600px' };

export const Login: React.FC<{ className: string }> = ({ className }) => {
  const [input, setInput] = React.useState('');
  const { setToken, setUser } = React.useContext(AuthorizationContext);

  const onSubmit = React.useCallback(() => {
    setToken(null);
    setUser(null);
  }, [setToken, setUser]);

  return (
    <div className={clsx(className, 'flex content-center')} style={pageStyle}>
      <div className="mx-auto self-center">
        <input
          className="padded mr-6"
          style={inputStyle}
          placeholder="Token"
          value={input}
          onChange={(e): void => setInput(e.target.value)}
        />
        <button className="padded bg-green-400" onClick={onSubmit}>
          Login
        </button>
      </div>
    </div>
  );
};
