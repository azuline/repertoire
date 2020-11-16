import * as React from 'react';

import { GlobalContexts } from 'src/contexts';

import { AuthorizationContext } from 'src/contexts';
import { BrowserRouter } from 'react-router-dom';
import { Footer } from 'src/components/Footer';
import { Header } from 'src/components/Header';
import { Login } from 'src/pages';
import { Routes } from 'src/Routes';

const App: React.FC = () => {
  return (
    <BrowserRouter>
      <GlobalContexts>
        <Body />
      </GlobalContexts>
    </BrowserRouter>
  );
};

const Body: React.FC = () => {
  const { token } = React.useContext(AuthorizationContext);

  return (
    <div className="app w-full min-h-screen flex flex-col">
      {!token ? (
        <Login className="flex-1" />
      ) : (
        <>
          <Header className="flex-none" />
          <Routes />
          <Footer />
        </>
      )}
    </div>
  );
};

export default App;
