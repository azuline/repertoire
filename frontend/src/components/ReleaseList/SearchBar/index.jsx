import './index.scss';

import { Button, InputGroup } from '@blueprintjs/core';
import React, { useContext } from 'react';

import { RecentQueries } from './RecentQueries';
import { SaveQuery } from './SaveQuery';
import { SearchContext } from 'contexts';

export const SearchBar = () => {
  const { query, runQuery, setQuery } = useContext(SearchContext);

  // An extra handler for the outer-form wrapper which prevents the form submission.
  const executeQueryForm = (event) => {
    runQuery(query);
    event.preventDefault();
  };

  return (
    <div className="SearchBar">
      <form className="InputForm" onSubmit={executeQueryForm}>
        <InputGroup
          className="SearchBarInput"
          value={query}
          onChange={(event) => setQuery(event.target.value)}
          large
          placeholder="Query"
          leftElement={<RecentQueries />}
          rightElement={
            <div className="RightElements">
              <Button minimal text="Clear" type="reset" onClick={() => runQuery('')} />
              <SaveQuery />
              <Button icon="arrow-right" intent="primary" onClick={executeQueryForm} />
            </div>
          }
        />
      </form>
    </div>
  );
};
