import { SearchContextProvider, ThemeContextProvider } from 'contexts';

import { BrowserRouter } from 'react-router-dom';
import { Header } from './Header';
import React from 'react';
import { RecentQueriesContextProvider } from 'contexts';
import { Routes } from './Routes';

export const App = () => {
  return (
    <BrowserRouter>
      <RecentQueriesContextProvider>
        <SearchContextProvider>
          <ThemeContextProvider>
            <div className="App">
              <Header />
              <Routes />
            </div>
          </ThemeContextProvider>
        </SearchContextProvider>
      </RecentQueriesContextProvider>
    </BrowserRouter>
  );
};
