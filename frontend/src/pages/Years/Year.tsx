import * as React from 'react';

import { SectionHeader } from '~/components';

import { YearReleases } from './Releases';

type IYear = React.FC<{ active: number }>;

export const Year: IYear = ({ active }) => {
  return (
    <div tw="flex flex-col w-full">
      <SectionHeader tw="mt-4 mb-8">Year: {active}</SectionHeader>
      <YearReleases active={active} />
    </div>
  );
};
