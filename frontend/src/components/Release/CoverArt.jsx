import { Icon, Position, Tooltip } from '@blueprintjs/core';
import React, { useContext, useEffect, useState } from 'react';

import { ThemeContext } from 'contexts';
import loading from 'images/loading.png';
import noArtDark from 'images/noArtDark.png';
import noArtLight from 'images/noArtLight.png';
import { useRequest } from 'hooks';

export const CoverArt = ({ inInbox, releaseId, hasImage }) => {
  const request = useRequest();
  const { dark } = useContext(ThemeContext);
  const [imageUrl, setImageUrl] = useState(loading);

  useEffect(() => {
    (async () => {
      // If there is no image, just return no art image.
      if (!hasImage) {
        setImageUrl(dark ? noArtDark : noArtLight);
        return;
      }

      // Otherwise, make a request for the image.
      try {
        const response = await request(`/files/covers/${releaseId}?thumbnail=true`);
        if (response.status !== 200) throw new Error('broked');
        const blob = await response.blob();
        setImageUrl(URL.createObjectURL(blob));
      } catch {
        setImageUrl(dark ? noArtDark : noArtLight);
      }
    })();
  }, [dark, request, releaseId, hasImage, setImageUrl]);

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
      <img src={imageUrl} alt="Cover Art" />
    </div>
  );
};
