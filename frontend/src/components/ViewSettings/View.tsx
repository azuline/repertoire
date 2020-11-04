import * as React from 'react';

import { RVOCType } from 'src/hooks';
import { Select } from 'src/components/common/Select';
import { ReleaseView } from 'src/types';

const displays: { [k in ReleaseView]: string } = {
  [ReleaseView.ARTWORK]: 'Artwork',
  [ReleaseView.ROW]: 'Row',
};

export const View: React.FC<{ viewOptions: RVOCType; className?: string }> = ({
  viewOptions,
  className = '',
}) => {
  // prettier-ignore
  const updateView = React.useCallback(
    (e) => viewOptions.setReleaseView(e.currentTarget.value),
    [viewOptions],
  );

  return (
    <Select onChange={updateView} label="View" name="select-view" className={className}>
      {Object.values(ReleaseView).map((value) => (
        <option key={value} value={value} selected={value === viewOptions.releaseView}>
          {displays[value]}
        </option>
      ))}
    </Select>
  );
};
