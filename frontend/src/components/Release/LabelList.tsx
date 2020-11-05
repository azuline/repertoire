import * as React from 'react';
import { Link } from 'src/components/common/Link';

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
          <Link href={`/labels/${lbl.id}`}>{lbl.name}</Link>
        </span>
      ))}
    </div>
  );
};
