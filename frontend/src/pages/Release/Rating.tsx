import { gql } from '@apollo/client';
import clsx from 'clsx';
import React from 'react';
import tw, { styled } from 'twin.macro';

import { Icon } from '~/components';
import { IRelease, useReleaseUpdateReleaseRatingMutation } from '~/graphql';

type IRating = React.FC<{ release: IRelease }>;

export const Rating: IRating = ({ release }) => {
  const [mutateRelease] = useReleaseUpdateReleaseRatingMutation();

  const setRating = (value: number): void => {
    mutateRelease({ variables: { id: release.id, rating: value } });
  };

  return (
    <Wrapper>
      {Array.from(new Array(10), (_, i) => {
        const active = release.rating !== null && i < release.rating;

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

/* eslint-disable */
gql`
  mutation ReleaseUpdateReleaseRating($id: Int!, $rating: Int) {
    updateRelease(id: $id, rating: $rating) {
      id
      rating
    }
  }
`;
