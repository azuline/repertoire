import * as React from 'react';

import { PickArtists } from './Artists';
import { RVOCType } from 'src/hooks';

type ChooserT = React.FC<{
  viewOptions: RVOCType;
  className?: string;
}>;

export const ArtistChooser: ChooserT = (props) => {
  return PickArtists({ ...props, picker: 'chooser' });
};

export const ArtistSelector: ChooserT = (props) => {
  return PickArtists({ ...props, picker: 'selector' });
};
