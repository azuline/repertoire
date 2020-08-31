import { Button, MenuItem } from '@blueprintjs/core';
import React, { useCallback, useContext } from 'react';

import { PaginationContext } from 'contexts';
import { Select } from '@blueprintjs/select';

const perPageOptions = [25, 50, 100];

export const PerPage = () => {
  const { perPage, setPerPage } = useContext(PaginationContext);

  const renderOption = useCallback(
    (perPage_) => {
      return (
        <MenuItem
          active={perPage_ === perPage}
          key={perPage_}
          onClick={() => setPerPage(perPage_)}
          text={`Per Page: ${perPage_}`}
        />
      );
    },
    [perPage, setPerPage]
  );

  return (
    <Select
      className="SelectPerPage"
      filterable={false}
      items={perPageOptions}
      itemRenderer={renderOption}
      popoverProps={{ minimal: true, transitionDuration: 50 }}
    >
      <Button text={perPage} icon="document" rightIcon="caret-down" />
    </Select>
  );
};
