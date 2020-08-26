import { Icon, Position, Tooltip } from '@blueprintjs/core';

import React from 'react';
import noArt from 'images/noArt.png';

export const CoverArt = ({ inInbox }) => {
  return (
    <div className="CoverArt">
      {inInbox && (
        <div className="InInbox">
          <Tooltip content="In Inbox!" position={Position.TOP}>
            <Icon
              className="InInboxIcon"
              icon="inbox-update"
              intent="danger"
              htmlTitle="In Inbox"
            />
          </Tooltip>
        </div>
      )}
      <img src={noArt} alt="No Cover Art" />
    </div>
  );
};
