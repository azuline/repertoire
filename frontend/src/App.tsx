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
        <div className="w-screen h-screen flex flex-col flex-no-wrap bg-gray-100">
          <Header />
          <Routes className="w-full flex-1" />
          <Footer />
        </div>
      </GlobalContexts>
    </BrowserRouter>
  );
};

export default App;
