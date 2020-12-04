import * as React from 'react';
import { Chooser } from 'src/components';
import { useFetchYears } from 'src/lib';

const urlFactory = (id: number): string => `/years/${id}`;

export const YearChooser: React.FC<{
  active: number | null;
  className?: string;
}> = ({ active, className }) => {
  const { data, error, loading } = useFetchYears();

  const elements =
    !data || error || loading
      ? []
      : data.releaseYears.map((year) => ({ id: year, name: `${year}` }));

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
