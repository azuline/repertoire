import * as React from 'react';

import { Chooser } from '~/components';
import { useFetchReleaseYearsQuery } from '~/graphql';

type IYearChooser = React.FC<{
  active: number | null;
  className?: string;
}>;

export const YearChooser: IYearChooser = ({ active, className }) => {
  const { data } = useFetchReleaseYearsQuery();

  const elements =
    data?.releaseYears
      ?.filter((year): year is number => year !== null)
      .map((year) => ({ id: year, name: `${year}` })) || [];

  return (
    <Chooser
      active={active}
      className={className}
      results={elements}
      starrable={false}
      toggleStarFactory={(): undefined => undefined}
      urlFactory={urlFactory}
    />
  );
};

const urlFactory = (id: number): string => `/years/${id}`;
