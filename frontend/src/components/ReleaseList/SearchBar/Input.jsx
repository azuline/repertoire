import { Button, InputGroup } from '@blueprintjs/core';
import React, { useContext } from 'react';
import { SearchContext } from 'contexts';

import { RecentQueries } from './RecentQueries';
import { SaveQuery } from './SaveQuery';
import { executeQuery } from 'lib/queries';

export const Input = () => {
  const { query, setQuery } = useContext(SearchContext);

  // An extra handler for the outer-form wrapper which prevents the form submission.
  const executeQueryForm = (event) => {
    executeQuery();
    event.preventDefault();
  };

  return (
    <form className="InputForm" onSubmit={executeQueryForm}>
      <InputGroup
        className="SearchBarInput"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        large
        placeholder="Query"
        leftElement={<RecentQueries />}
        rightElement={
          <div className="RightElements">
            <Button minimal text="Clear" type="reset" onClick={() => setQuery('')} />
            <SaveQuery />
            <Button icon="arrow-right" intent="primary" onClick={executeQuery} />
          </div>
        }
      />
    </form>
  );
};
