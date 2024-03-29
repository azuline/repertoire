import * as React from 'react';
import tw, { styled } from 'twin.macro';

import { Image } from '~/components/Image';
import { BackgroundContext } from '~/contexts';

/**
 * The inner background gradient covers the whole image. It works nicely on small-width
 * screens to provide a fade-out on the image.
 *
 * The outer background gradient covers the bottom of the image. It prevents the
 * blown-up image from drawing too much focus on large-width screens.
 */

export const Background: React.FC = () => {
  const { backgroundImageId } = React.useContext(BackgroundContext);

  if (backgroundImageId === null) {
    return null;
  }

  return (
    <div tw="absolute top-0 left-0 full overflow-hidden">
      <div tw="relative w-full h-0 overflow-hidden pb-full">
        <Image imageId={backgroundImageId} tw="object-cover w-full opacity-50" />
        <InnerBackground />
      </div>
      <OuterBackground />
    </div>
  );
};

const OuterBackground = styled.div`
  ${tw`absolute top-0 left-0 full`}

  background: linear-gradient(
    180deg,
    rgba(16, 16, 19, 0.2),
    rgba(16, 16, 19, 0.7),
    rgba(16, 16, 19, 0.9),
    rgba(16, 16, 19, 1),
    rgba(16, 16, 19, 1),
    rgba(16, 16, 19, 1)
  );
`;

const InnerBackground = styled.div`
  ${tw`absolute top-0 left-0 full`}

  background: linear-gradient(
    190deg,
    rgba(16, 16, 19, 0.6),
    rgba(16, 16, 19, 0.7),
    rgba(16, 16, 19, 0.8),
    rgba(16, 16, 19, 1),
    rgba(16, 16, 19, 1)
  );
`;
