import './index.scss';

import { Button, InputGroup } from '@blueprintjs/core';
import React, { useCallback, useContext, useState } from 'react';

import { AuthenticationContext } from 'contexts';
import { useRequest } from 'hooks';

export const Login = () => {
  const request = useRequest();
  const [input, setInput] = useState('');
  const { setToken, setUsername } = useContext(AuthenticationContext);

  const auth = useCallback(
    (token) => {
      (async () => {
        const response = await request('/api/user', {
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
    [request, setToken, setUsername]
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
