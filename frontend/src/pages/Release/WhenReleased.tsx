import * as React from 'react';

import { Link } from '~/components';
import { IRelease } from '~/graphql';
import { formatDate } from '~/util';

type IWhenReleased = React.FC<{
  release: Pick<IRelease, 'releaseDate' | 'releaseYear'>;
}>;

export const WhenReleased: IWhenReleased = ({ release }) => {
  if (release.releaseDate !== null) {
    return (
      <>
        <span tw="text-foreground-300">Released on </span>
        <span>{formatDate(new Date(release.releaseDate))}</span>
      </>
    );
  }

  if (release.releaseYear !== null) {
    return (
      <>
        <span tw="text-foreground-300">Released in </span>
        <Link href={`/years/${release.releaseYear}`} tw="text-primary-400">
          {release.releaseYear}
        </Link>
      </>
    );
  }

  return <span tw="text-foreground-300">Released on unknown date</span>;
};
