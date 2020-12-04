import * as React from 'react';
import { Select } from 'src/components/common';
import { ViewOptionsT } from 'src/hooks';
import { ReleaseView } from 'src/types';

const displays: { [k in ReleaseView]: string } = {
  [ReleaseView.ARTWORK]: 'Artwork',
  [ReleaseView.ROW]: 'Row',
};

export const View: React.FC<{ viewOptions: ViewOptionsT; className?: string }> = ({
  viewOptions,
  className,
}) => {
  const onChange = (e: React.FormEvent<HTMLSelectElement>): void =>
    viewOptions.setReleaseView(e.currentTarget.value as ReleaseView);

  return (
    <Select
      className={className}
      label="View"
      name="select-view"
      value={viewOptions.releaseView}
      onChange={onChange}
    >
      {Object.values(ReleaseView).map((value) => (
        <option key={value} value={value}>
          {displays[value]}
        </option>
      ))}
    </Select>
  );
};
