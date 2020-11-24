import * as React from 'react';

import { Header } from 'src/components/Header';
import { useId } from 'src/hooks';

export const Release: React.FC = () => {
  const id = useId();

  return (
    <div className="flex flex-col full">
      <Header />
      <div className="px-8 mt-4">You are viewing release {id}.</div>
    </div>
  );
};
