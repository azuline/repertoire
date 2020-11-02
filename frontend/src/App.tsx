import * as React from 'react';
import { Header } from 'src/components/Header';
import { BrowserRouter } from 'react-router-dom';
import { Footer } from 'src/components/Footer';
import { GlobalContexts } from 'src/contexts';
import { Routes } from 'src/Routes';

const App: React.FC = (): React.ReactElement => {
  return (
    <BrowserRouter>
      <GlobalContexts>
        <div className="app w-full flex flex-col bg-gray-100">
          <Header />
          <Routes className="flex-1 mt-8 w-11/12 mx-auto pb-24" />
          <Footer />
        </div>
      </GlobalContexts>
    </BrowserRouter>
  );
};

export default App;
