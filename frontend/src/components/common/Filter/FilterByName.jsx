import { Button, InputGroup } from '@blueprintjs/core';
import React, { useContext } from 'react';

import { FilterContext } from 'components/Contexts';

export const FilterByName = () => {
  const { filter, updateFilter } = useContext(FilterContext);

  return (
    <InputGroup
      className="FilterByName"
      placeholder="Filter by name... (uses regex)"
      leftIcon="highlight"
      rightElement={
        <Button
          minimal
          text="Clear"
          type="reset"
          onClick={() => updateFilter({ filter: '' })}
        />
      }
      value={filter}
      onChange={(event) => updateFilter({ filter: event.target.value })}
    />
  );
};
