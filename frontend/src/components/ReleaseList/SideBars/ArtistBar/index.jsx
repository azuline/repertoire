import React, { useContext } from 'react';
import { SearchContext, ArtistsContext } from 'contexts';
import { Entry } from './Entry';
import { Card } from '@blueprintjs/core';

export const ArtistBar = ({ hidden }) => {
  const { artists } = useContext(ArtistsContext);
  const { artists: activeArtists } = useContext(SearchContext);

  return (
    <Card className={'SideBar ArtistBar' + (hidden ? ' Hidden' : '')}>
      <Card className="SideBarHeader">Artists</Card>
      {artists.map((artist) => (
        <Entry key={artist.id} artist={artist} activeArtists={activeArtists} />
      ))}
    </Card>
  );
};
