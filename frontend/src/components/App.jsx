import { BrowserRouter } from 'react-router-dom';
import { Header } from './Header';
import { Contexts } from './Contexts';
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
