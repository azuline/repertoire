import * as React from 'react';

import noArt from 'src/assets/noArt.jpg';

export const CoverArt: React.FC<{
  className: string;
  release: { id: number; hasCover: boolean };
}> = ({ className, release: { id, hasCover } }) => {
  const [src, setSrc] = React.useState(`/files/covers/${id}?thumbnail=true`);
  const onError = React.useCallback(() => setSrc(noArt), [setSrc]);

  if (!hasCover) {
    return <img className={className} src={noArt} />;
  } else {
    return <img className={className} src={src} onError={onError} loading="lazy" />;
  }
};
