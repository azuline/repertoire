import clsx from 'clsx';
import * as React from 'react';
import tw, { styled } from 'twin.macro';

import { Icon } from '~/components';
import { IRelease, useUpdateReleaseRatingMutation } from '~/graphql';

export const Rating: React.FC<{ release: IRelease }> = ({ release }) => {
  const [mutateRelease] = useUpdateReleaseRatingMutation();

  const setRating = (value: number): void => {
    mutateRelease({ variables: { id: release.id, rating: value } });
  };

  return (
    <Wrapper>
      {Array.from(new Array(10), (_, i) => {
        const active = release.rating && i < release.rating;

        return (
          <Icon
            key={i}
            className={clsx('star', active ? 'active' : 'inactive')}
            icon="star-medium"
            tw="cursor-pointer w-7 pr-0.5"
            onClick={(): void => setRating(i + 1)}
          />
        );
      })}
    </Wrapper>
  );
};

const Wrapper = styled.div`
  ${tw`flex items-center`}

  .star {
    ${tw`text-gray-500`}

    &.inactive {
      ${tw`stroke-current fill-transparent`}
    }

    &.active {
      ${tw`fill-current text-primary-400`}
    }
  }

  &:hover {
    & > .star {
      ${tw`fill-current stroke-current text-primary-400`}
    }
    & > .star:hover ~ .star {
      ${tw`text-gray-500 stroke-current fill-transparent`}
    }
  }
`;
