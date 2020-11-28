import * as React from 'react';
import { Image } from 'src/components/Image';
import { BackgroundContext } from 'src/contexts';

// TODO: Light theme-ify support this.
const backgroundStyle = {
  background:
    'linear-gradient(185deg, rgba(16, 16, 19, 0.5), rgba(16, 16, 19, 0.6), rgba(16, 16, 19, 0.8), rgba(16, 16, 19, 1), rgba(16, 16, 19, 1))',
};

export const Background: React.FC = () => {
  const { backgroundImageId } = React.useContext(BackgroundContext);

  if (backgroundImageId === null) return null;

  return (
    <div className="absolute top-0 left-0 h-0 full">
      <div className="absolute top-0 left-0 z-0 opacity-50 full">
        <Image className="object-cover full" imageId={backgroundImageId} />
      </div>
      <div className="absolute top-0 left-0 z-0 max-h-screen full" style={backgroundStyle} />
    </div>
  );
};
