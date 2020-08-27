import { Icon, Position, Tooltip } from '@blueprintjs/core';
import { ThemeContext } from 'contexts';

import React, { useContext } from 'react';
import noArtLight from 'images/noArtLight.png';
import noArtDark from 'images/noArtDark.png';

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
