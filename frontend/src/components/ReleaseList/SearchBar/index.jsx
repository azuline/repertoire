import './index.scss';

import { Button, InputGroup } from '@blueprintjs/core';
import React, { useCallback, useContext } from 'react';

import { RecentQueries } from './RecentQueries';
import { SaveQuery } from './SaveQuery';
import { SearchContext } from 'contexts';

export const SearchBar = () => {
  const { query, setActiveQuery, setQuery } = useContext(SearchContext);

  // An extra handler for the outer-form wrapper which prevents the form submission.
  const executeQueryForm = useCallback(
    (event) => {
      setActiveQuery(query);
      event.preventDefault();
    },
    [query, setActiveQuery]
  );

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
              <Button
                minimal
                text="Clear"
                type="reset"
                onClick={() => setActiveQuery('')}
              />
              <SaveQuery />
              <Button icon="arrow-right" intent="primary" onClick={executeQueryForm} />
            </div>
          }
        />
      </form>
    </div>
  );
};
