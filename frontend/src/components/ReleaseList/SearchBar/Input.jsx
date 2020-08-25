import { Button, Icon, InputGroup } from '@blueprintjs/core';
import React, { useContext } from 'react';
import { RecentQueriesContext, SearchContext } from 'components/Contexts';

import { RecentQueries } from './RecentQueries';

export const Input = () => {
  const { query, setQuery } = useContext(SearchContext);
  const { updateRecentQueries } = useContext(RecentQueriesContext);

  const executeQuery = () => {
    updateRecentQueries(query);
  };

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
        leftElement={
          <div className="LeftElements">
            <Icon icon="search" />
            <RecentQueries />
          </div>
        }
        rightElement={
          <div className="RightElements">
            <Button minimal text="Clear" type="reset" onClick={() => setQuery('')} />
            <Button icon="arrow-right" intent="primary" onClick={executeQuery} />
          </div>
        }
      />
    </form>
  );
};
