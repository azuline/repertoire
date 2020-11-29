import * as React from 'react';
import ReactSlider from 'react-slider';
import { Icon, IconT } from 'src/components/common';
import { VolumeContext } from 'src/contexts';

export const VolumeControl: React.FC = () => {
  const { volume, setVolume, isMuted, setIsMuted } = React.useContext(VolumeContext);

  const icon = React.useMemo(() => (isMuted ? 'volume-off-small' : 'volume-up-small'), [isMuted]);
  const toggleMute = React.useCallback(() => setIsMuted((m) => !m), [setIsMuted]);
  const onSliderChange = React.useCallback((value) => (!value ? setVolume(0) : setVolume(value)), [
    setVolume,
  ]);

  return (
    <div className="relative hidden mr-1 sm:block hover-popover">
      <div className="p-2 cursor-pointer text-primary-600 hover:text-primary-400" onClick={toggleMute}>
        <Icon className="w-6" icon={icon as IconT} />
      </div>
      <div className="absolute w-10 h-56 px-2 py-4 border-2 border-gray-300 rounded-lg -top-56 bg-background-900 dark:border-gray-700">
        <ReactSlider
          className="slider volume-slider"
          value={volume}
          onChange={onSliderChange}
          orientation="vertical"
          invert
        />
      </div>
    </div>
  );
};
