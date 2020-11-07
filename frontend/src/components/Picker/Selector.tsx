import * as React from 'react';

import { ElementT } from './Element';
import { Select } from 'src/components/common/Select';
import clsx from 'clsx';

export const Selector: React.FC<{
  className?: string;
  setter: (arg0: number[]) => void;
  results: ElementT[];
}> = ({ className = '', setter, results }) => {
  const [active, setActive] = React.useState<number | null>(null);

  React.useEffect(() => setter(active ? [active] : []), [active]);

  const updateActive = React.useCallback((e) => setActive(parseInt(e.currentTarget.value)), [
    setActive,
  ]);

  return (
    <Select
      value={active || ''}
      onChange={updateActive}
      label="Artist"
      name="select-artist"
      className={clsx(className, 'mx-1/24')}
      selectClassName="py-4"
    >
      {results.map((elem: ElementT) => (
        <option key={elem.id} value={elem.id}>
          {elem.name}
        </option>
      ))}
    </Select>
  );
};
