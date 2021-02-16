import * as React from 'react';
import { styled } from 'twin.macro';

import { ArtRelease } from '~/components/Release';
import { IRelease } from '~/graphql';

export const ScrolledReleases: React.FC<{
  releases: IRelease[];
  className?: string;
}> = ({ releases }) => (
  <Wrapper tw="w-fullpad px-6 md:px-8 -mx-6 md:-mx-8 py-8 flex overflow-x-auto">
    {releases.map((rls) => (
      <div key={rls.id} tw="flex-shrink-0 w-56 h-56 mr-4">
        <ArtRelease release={rls} />
      </div>
    ))}
  </Wrapper>
);

const Wrapper = styled.div`
  &:after {
    content: '';
    flex: 0 0 2rem;
    margin: 0 0 0 -1rem;
  }
`;
