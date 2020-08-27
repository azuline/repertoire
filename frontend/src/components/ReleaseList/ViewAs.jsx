import { Button, ControlGroup, MenuItem } from '@blueprintjs/core';
import React, { useContext } from 'react';

import { Select } from '@blueprintjs/select';
import { ViewContext } from 'contexts';

export const ViewAs = ({ criteria }) => {
  const { view, expandTrackLists, setView, setExpandTrackLists } = useContext(
    ViewContext
  );

  const renderCriteria = (view_) => {
    return (
      <MenuItem
        active={view_ === view}
        key={view_}
        onClick={() => setView(view_)}
        text={view_}
      />
    );
  };

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
        disabled={view === 'Artwork'}
        icon="expand-all"
        onClick={() => setExpandTrackLists(!expandTrackLists)}
      >
        {expandTrackLists ? 'Collapse Tracks' : 'Expand Tracks'}
      </Button>
    </ControlGroup>
  );
};
