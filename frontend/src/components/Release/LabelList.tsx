import * as React from 'react';

import { CollectionT } from 'src/types';
import clsx from 'clsx';

export const LabelList: React.FC<{
  labels: CollectionT[] | undefined;
  className?: string;
  prefix?: string;
}> = ({ labels, className = '', prefix = '' }) => {
  if (!labels || labels.length === 0) return null;

  return (
    <div className={clsx(className, 'flex')}>
      {prefix && <span>{prefix}&nbsp;</span>}
      {labels.map((lbl, i) => (
        <span key={lbl.id}>
          {i > 0 && ', '}
          <a href={`/labels/${lbl.id}`}>{lbl.name}</a>
        </span>
      ))}
    </div>
  );
};
