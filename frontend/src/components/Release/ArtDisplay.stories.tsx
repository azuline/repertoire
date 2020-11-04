import * as React from 'react';

import { ArtRelease } from './ArtDisplay';
import { Story } from '@storybook/react/types-6-0';

export default {
  title: 'ArtRelease',
  component: ArtRelease,
};

const Template: Story<React.ComponentProps<typeof ArtRelease>> = (props) => (
  <ArtRelease {...props} />
);

export const Simple = Template.bind({});
Simple.args = {
  release: {
    id: 1,
    title: "I have no idea wtf I'm doing lol!",
    releaseType: 'ALBUM',
    addedOn: 1603756679,
    inInbox: true,
    releaseYear: 2020,
    numTracks: 17,
    releaseDate: '2020-10-26',
    hasCover: false,
    artists: [{ id: 1, name: 'Web design is my passion!', favorite: false, numReleases: 9 }],
  },
};
