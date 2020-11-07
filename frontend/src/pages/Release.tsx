import * as React from 'react';
import { useId } from 'src/hooks';

export const Release: React.FC = () => {
  const id = useId();

  return <div className="px-8 py-6">You are viewing release {id}.</div>;
};
