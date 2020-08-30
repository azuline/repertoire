import { Button, ControlGroup, MenuItem } from '@blueprintjs/core';
import React, { useCallback, useContext } from 'react';

import { Select } from '@blueprintjs/select';
import { ViewContext } from 'contexts';

export const ViewAs = ({ criteria }) => {
  const { view, setView, expandTrackLists, setExpandTrackLists } = useContext(
    ViewContext
  );

  const renderCriteria = useCallback(
    (view_) => {
      return (
        <MenuItem
          active={view_ === view}
          key={view_}
          onClick={() => setView(view_)}
          text={view_}
        />
      );
    },
    [view, setView]
  );

  return (
    <ControlGroup className="ViewAs">
      <Select
        className="SelectView"
        filterable={false}
        items={criteria}
        itemRenderer={renderCriteria}
        popoverProps={{ minimal: true, transitionDuration: 50 }}
      >
        <Button text={view} icon="eye-open" rightIcon="caret-down" />
      </Select>
      <Button
        className="ExpandTracks"
        disabled={view === 'Artwork'}
        icon={expandTrackLists ? 'collapse-all' : 'expand-all'}
        onClick={() => setExpandTrackLists(!expandTrackLists)}
      >
        {expandTrackLists ? 'Collapse Tracks' : 'Expand Tracks'}
      </Button>
    </ControlGroup>
  );
};
