import clsx from 'clsx';
import * as React from 'react';

import { Icon } from '~/components';
import { IRelease } from '~/graphql';
import { useMutateRelease } from '~/lib';

export const Rating: React.FC<{ release: IRelease }> = ({ release }) => {
  const [mutateRelease] = useMutateRelease();

  const setRating = (value: number): void => {
    mutateRelease({ variables: { id: release.id, rating: value } });
  };

  return (
    <div className="flex items-center release-ratings">
      {Array.from(new Array(10), (_, i) => {
        const active = release.rating && i < release.rating;

        return (
          <Icon
            key={i}
            className={clsx(
              'cursor-pointer w-7 pr-0.5 star',
              active ? 'star-active' : 'star-inactive',
            )}
            icon="star-medium"
            onClick={(): void => setRating(i + 1)}
          />
        );
      })}
    </div>
  );
};
