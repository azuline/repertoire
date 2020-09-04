import './index.scss';

import { Button, InputGroup } from '@blueprintjs/core';
import React, { useCallback, useContext, useRef } from 'react';

import { RecentQueries } from './RecentQueries';
import { SaveQuery } from './SaveQuery';
import { SearchContext } from 'contexts';
import { useEffect } from 'react';

export const SearchBar = () => {
  const inputRef = useRef();
  const { query, setQuery } = useContext(SearchContext);

  // An extra handler for the outer-form wrapper which prevents the form submission.
  const executeQueryForm = useCallback(
    (event) => {
      setQuery(inputRef ? inputRef.current.value ?? '' : '');
      event.preventDefault();
    },
    [inputRef, setQuery]
  );

  // Update input value when search context's query is updated
  useEffect(() => {
    inputRef.current.value = query;
  }, [query]);

  const clearQuery = useCallback(() => setQuery(''), [setQuery]);

  return (
    <div className="SearchBar">
      <form className="InputForm" onSubmit={executeQueryForm}>
        <InputGroup
          className="SearchBarInput"
          name="search"
          large
          placeholder="Query"
          leftElement={<RecentQueries />}
          inputRef={inputRef}
          rightElement={
            <div className="RightElements">
              <Button minimal text="Clear" type="reset" onClick={clearQuery} />
              <SaveQuery />
              <Button icon="arrow-right" intent="primary" onClick={executeQueryForm} />
            </div>
          }
        />
      </form>
    </div>
  );
};
