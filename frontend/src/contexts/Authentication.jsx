import React from 'react';
import { usePersistentState } from 'hooks';

export const AuthenticationContext = React.createContext({
  token: '',
});

export const AuthenticationContextProvider = ({ children }) => {
  const [token, setToken] = usePersistentState('auth--token', '');
  const [username, setUsername] = usePersistentState('auth--username', '');

  const value = { token, setToken, username, setUsername };

  return (
    <AuthenticationContext.Provider value={value}>
      {children}
    </AuthenticationContext.Provider>
  );
};
