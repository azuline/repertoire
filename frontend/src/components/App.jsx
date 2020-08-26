import React, { useState } from 'react';

import { BrowserRouter } from 'react-router-dom';
import { Header } from './Header';
import { Routes } from './Routes';
import { SearchContext } from 'contexts';

export const App = () => {
  const [query, setQuery] = useState('');
  const searchValue = { query: query, setQuery: setQuery };

  return (
    <BrowserRouter>
      <SearchContext.Provider value={searchValue}>
        <div className="App">
          <Header />
          <Routes />
        </div>
      </SearchContext.Provider>
    </BrowserRouter>
  );
};
