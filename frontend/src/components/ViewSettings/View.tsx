import React from 'react';

import { Select } from '~/components/common';
import { IViewOptions } from '~/hooks';
import { IReleaseView } from '~/types';

const displays: { [k in IReleaseView]: string } = {
  [IReleaseView.Artwork]: 'Artwork',
  [IReleaseView.Row]: 'Row',
};

type IView = React.FC<{ viewOptions: IViewOptions; className?: string }>;

export const View: IView = ({ viewOptions, className }) => {
  const onChange = (e: React.FormEvent<HTMLSelectElement>): void =>
    viewOptions.setReleaseView(e.currentTarget.value as IReleaseView);

  return (
    <Select
      className={className}
      label="View"
      name="select-view"
      value={viewOptions.releaseView}
      onChange={onChange}
    >
      {Object.values(IReleaseView).map((value) => (
        <option key={value} value={value}>
          {displays[value]}
        </option>
      ))}
    </Select>
  );
};
