import { Icon, Position, Tooltip } from '@blueprintjs/core';
import React, { useContext } from 'react';

import { ThemeContext } from 'contexts';
import noArtDark from 'images/noArtDark.png';
import noArtLight from 'images/noArtLight.png';

export const CoverArt = ({ inInbox }) => {
  const { dark } = useContext(ThemeContext);

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
      <img src={dark ? noArtDark : noArtLight} alt="No Cover Art" />
    </div>
  );
};
