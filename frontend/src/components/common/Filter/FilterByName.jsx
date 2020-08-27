import { Button, InputGroup } from '@blueprintjs/core';
import React, { useContext } from 'react';

import { FilterContext } from 'contexts';

export const FilterByName = () => {
  const { filter, setFilter } = useContext(FilterContext);

  return (
    <InputGroup
      className="FilterByName"
      placeholder="Filter by name (fuzzy)..."
      leftIcon="highlight"
      rightElement={
        <Button minimal text="Clear" type="reset" onClick={() => setFilter('')} />
      }
      value={filter}
      onChange={(event) => setFilter(event.target.value)}
    />
  );
};
