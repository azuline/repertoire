import React, { useState } from 'react';

import { BrowserRouter } from 'react-router-dom';
import { Header } from './Header';
import { Routes } from './Routes';
import { SearchContext, ThemeContext } from 'contexts';
import { useThemeContext } from 'hooks';

const localDark = localStorage.getItem('theme-dark');

export const App = () => {
  const [query, setQuery] = useState('');
  const searchValue = { query: query, setQuery: setQuery };

  const [, themeValue] = useThemeContext(localDark);

  return (
    <BrowserRouter>
      <SearchContext.Provider value={searchValue}>
        <ThemeContext.Provider value={themeValue}>
          <div className="App">
            <Header />
            <Routes />
          </div>
        </ThemeContext.Provider>
      </SearchContext.Provider>
    </BrowserRouter>
  );
};
