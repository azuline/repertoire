import * as React from 'react';
import tw, { styled } from 'twin.macro';

import { Icon, Slider } from '~/components/common';
import { VolumeContext } from '~/contexts';

export const VolumeControl: React.FC = () => {
  const { volume, setVolume, isMuted, setIsMuted } = React.useContext(VolumeContext);

  const icon = isMuted ? 'volume-off-small' : 'volume-up-small';

  return (
    <Wrapper>
      <div
        tw="p-2 cursor-pointer hover:text-primary-400 text-primary-500"
        onClick={(): void => setIsMuted((m) => !m)}
      >
        <Icon icon={icon} tw="w-6" />
      </div>
      <VolumeSlider>
        <Slider
          invert
          orientation="vertical"
          value={volume}
          onChange={(value): void => setVolume(value as number)}
        />
      </VolumeSlider>
    </Wrapper>
  );
};

const Wrapper = styled.div`
  ${tw`relative hidden mr-1 sm:block`}

  &:not(:hover) > :nth-of-type(2) {
    display: none;
  }
`;

const VolumeSlider = styled.div`
  ${tw`
    absolute
    -top-56
    w-10
    h-56
    px-2
    py-4
    border-2
    border-gray-300
    rounded-lg
    bg-background-900
    dark:border-gray-700
  `}

  .slider .track {
    ${tw`w-2 rounded-lg`}
  }
`;
