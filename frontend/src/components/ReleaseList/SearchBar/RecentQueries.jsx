import { Button, Menu, MenuItem } from '@blueprintjs/core';
import React, { useContext } from 'react';
import { RecentQueriesContext, SearchContext } from 'contexts';

import { Select } from '@blueprintjs/select';
import { formatDate } from 'common/datetime';

export const RecentQueries = () => {
  const { recentQueries } = useContext(RecentQueriesContext);
  const { setQuery } = useContext(SearchContext);

  const renderItem = ([index, { query, time }]) => {
    return (
      <MenuItem
        key={query}
        label={formatDate(time)}
        onClick={() => setQuery(query)}
        text={`${index + 1}. ${query}`}
      />
    );
  };

  return (
    <Select
      className="RecentQueries"
      filterable={false}
      items={[...recentQueries.entries()]}
      itemRenderer={renderItem}
      popoverProps={{
        minimal: true,
        popoverClassName: 'RecentQueriesPopover',
        transitionDuration: 50,
      }}
      noResults={
        <Menu minimal className="NoResults">
          <MenuItem disabled text="No Recent Queries" />
        </Menu>
      }
    >
      <Button icon="chevron-down" minimal />
    </Select>
  );
};
