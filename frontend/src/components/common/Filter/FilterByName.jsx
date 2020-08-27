import { Button, InputGroup } from '@blueprintjs/core';
import { FilterContext, SortContext } from 'contexts';
import React, { useContext } from 'react';

export const FilterByName = () => {
  const { filter, setFilter } = useContext(FilterContext);
  const { defaultSortField, setSortField, setAsc } = useContext(SortContext);

  const onChange = (event) => {
    setFilter(event.target.value);

    if (event.target.value) {
      setSortField('Fuzzy Score');
      setAsc(true);
    } else {
      setSortField(defaultSortField);
    }
  };

  return (
    <InputGroup
      className="FilterByName"
      placeholder="Filter by name (fuzzy)..."
      leftIcon="highlight"
      rightElement={
        <Button minimal text="Clear" type="reset" onClick={() => setFilter('')} />
      }
      value={filter}
      onChange={onChange}
    />
  );
};
