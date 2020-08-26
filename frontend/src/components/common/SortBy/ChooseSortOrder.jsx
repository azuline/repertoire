import { Button, ButtonGroup } from '@blueprintjs/core';
import React, { useContext } from 'react';

import { SortContext } from 'contexts';

export const ChooseSortOrder = () => {
  const { asc, updateSort } = useContext(SortContext);

  return (
    <ButtonGroup className="SortOrder">
      <Button
        active={asc}
        onClick={() => updateSort({ asc: true })}
        icon="circle-arrow-up"
      >
        Asc
      </Button>
      <Button
        active={!asc}
        onClick={() => updateSort({ asc: false })}
        icon="circle-arrow-down"
      >
        Desc
      </Button>
    </ButtonGroup>
  );
};
