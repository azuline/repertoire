import React, { useCallback, useContext } from 'react';
import { SideBarContext } from 'contexts';

export const DarkOverlay = () => {
  const { setHideCollection, setHideArtist } = useContext(SideBarContext);

  const onClick = useCallback(() => {
    setHideCollection(true);
    setHideArtist(true);
  }, [setHideCollection, setHideArtist]);

  return <div onClick={onClick} className="DarkOverlay" />;
};
