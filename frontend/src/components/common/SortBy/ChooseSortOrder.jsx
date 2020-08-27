import { Button, ButtonGroup } from '@blueprintjs/core';
import React, { useContext } from 'react';

import { SortContext } from 'contexts';

export const ChooseSortOrder = () => {
  const { asc, setAsc } = useContext(SortContext);

  return (
    <ButtonGroup className="SortOrder">
      <Button active={asc} onClick={() => setAsc(true)} icon="circle-arrow-up">
        Asc
      </Button>
      <Button active={!asc} onClick={() => setAsc(false)} icon="circle-arrow-down">
        Desc
      </Button>
    </ButtonGroup>
  );
};
