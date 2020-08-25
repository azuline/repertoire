import './index.scss';

import React from 'react';
import { SavedQuery } from './SavedQuery';
import { mockQueries } from 'mockData';

export const Queries = () => {
  return (
    <div className="QueryList">
      {mockQueries.map((query) => (
        <SavedQuery key={query.id} query={query} />
      ))}
    </div>
  );
};
