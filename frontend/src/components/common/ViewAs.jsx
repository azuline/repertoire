import { Button, ControlGroup, MenuItem } from '@blueprintjs/core';
import React, { useContext } from 'react';

import { Select } from '@blueprintjs/select';
import { ViewContext } from 'components/Contexts';

export const ViewAs = ({ criteria }) => {
  const { view, expandTrackLists, updateView } = useContext(ViewContext);

  const renderCriteria = (view_) => {
    return (
      <MenuItem
        active={view_ === view}
        key={view_}
        onClick={() => updateView({ view: view_ })}
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
        onClick={() => updateView({ expandTrackLists: !expandTrackLists })}
      >
        {expandTrackLists ? 'Collapse Tracks' : 'Expand Tracks'}
      </Button>
    </ControlGroup>
  );
};
