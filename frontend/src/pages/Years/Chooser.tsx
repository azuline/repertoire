import { gql } from '@apollo/client';
import * as React from 'react';

import { BasicElement, Chooser, Link, NoChooserOption } from '~/components';
import { useYearsFetchReleaseYearsQuery } from '~/graphql';

type IYearChooser = React.FC<{
  active: number | null;
  className?: string;
}>;

export const YearChooser: IYearChooser = ({ active, className }) => {
  const { data } = useYearsFetchReleaseYearsQuery();

  const years =
    data?.releaseYears
      ?.filter((year): year is number => year !== null)
      .map((year) => ({ id: year, name: `${year}` })) || [];

  const renderElement = (index: number): React.ReactNode => {
    const element = years[index];

    return (
      <Link href={`years${element.id}`}>
        <BasicElement isActive={element.id === active}>{element.name}</BasicElement>
      </Link>
    );
  };

  if (years.length === 0) {
    return <NoChooserOption>No years :(</NoChooserOption>;
  }

  return (
    <Chooser
      active={active}
      className={className}
      renderElement={renderElement}
      results={years}
    />
  );
};

/* eslint-disable */
gql`
  query YearsFetchReleaseYears {
    releaseYears
  }
`;
