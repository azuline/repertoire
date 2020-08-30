import React, { useCallback, useState, useContext } from 'react';
import { Button, InputGroup } from '@blueprintjs/core';
import './index.scss';
import { AuthenticationContext } from 'contexts';
import { apiUrl } from 'requests';

export const Login = () => {
  const [input, setInput] = useState('');
  const { setToken, setUsername } = useContext(AuthenticationContext);

  const auth = useCallback(
    (token) => {
      (async () => {
        const response = await fetch(`${apiUrl}/api/user`, {
          headers: new Headers({ Authorization: `Token ${token}` }),
        });
        if (response.status !== 200) {
          // TODO: Use error component on failure.
        } else {
          const { username } = await response.json();
          setUsername(username);
          setToken(token);
        }
      })();
    },
    [setToken, setUsername]
  );

  return (
    <div className="Login">
      <form className="LoginForm" onSubmit={() => auth(input)}>
        <InputGroup
          className="LoginToken"
          placeholder="Enter login token"
          value={input}
          onChange={(event) => setInput(event.target.value)}
        />
        <Button icon="arrow-right" intent="success" onClick={() => auth(input)} />
      </form>
    </div>
  );
};
