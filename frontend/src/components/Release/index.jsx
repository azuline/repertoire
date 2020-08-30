import React, { useContext, useMemo } from 'react';

import { ArtworkRelease } from './ArtworkRelease';
import { CompactRelease } from './CompactRelease';
import { DetailedRelease } from './DetailedRelease';
import { ViewContext } from 'contexts';

export const Release = (props) => {
  const { view } = useContext(ViewContext);

  const ReleaseType = useMemo(() => {
    switch (view) {
      case 'Artwork':
        return ArtworkRelease;
      case 'Compact':
        return CompactRelease;
      case 'Detailed':
      default:
        return DetailedRelease;
    }
  }, [view]);

  const inInbox = useMemo(() => {
    return props.collections.some((collection) => collection.id === 1);
  }, [props.collections]);

  return <ReleaseType {...props} inInbox={inInbox} />;
};
