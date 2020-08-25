import React, { useContext, useMemo } from 'react';

import { ArtworkRelease } from './ArtworkRelease';
import { CompactRelease } from './CompactRelease';
import { DetailedRelease } from './DetailedRelease';
import { ViewContext } from 'components/Contexts';

export const Release = (props) => {
  const { view } = useContext(ViewContext);

  let ReleaseType;

  switch (view) {
    case 'Artwork':
      ReleaseType = ArtworkRelease;
      break;
    case 'Compact':
      ReleaseType = CompactRelease;
      break;
    case 'Detailed':
    default:
      ReleaseType = DetailedRelease;
      break;
  }

  const inInbox = useMemo(() => {
    return props.collections.some((collection) => collection.id === 1);
  }, [props.collections]);

  return <ReleaseType {...props} inInbox={inInbox} />;
};
