import { BrowserRouter } from 'react-router-dom';
import { Contexts } from './Contexts';
import { Header } from './Header';
import React from 'react';
import { Routes } from './Routes';

export const App = () => {
  return (
    <BrowserRouter>
      <Contexts>
        <div className="App">
          <Header />
          <Routes />
        </div>
      </Contexts>
    </BrowserRouter>
  );
};
