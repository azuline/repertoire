import * as React from 'react';
import { Header } from 'components/Header';
import { BrowserRouter } from 'react-router-dom';
import { Footer } from 'components/Footer';
import { Toaster } from 'components/Toaster';
import { GlobalContexts } from 'contexts';
import { Routes } from './Routes';

const App: React.FC = (): React.ReactElement => {
  return (
    <BrowserRouter>
      <GlobalContexts>
        <div className="w-screen h-screen flex flex-col flex-no-wrap bg-gray-100">
          <Toaster />
          <Header />
          <Routes className="w-full flex-1" />
          <Footer />
        </div>
      </GlobalContexts>
    </BrowserRouter>
  );
};

export default App;
