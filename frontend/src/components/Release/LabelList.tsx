import * as React from 'react';
import { Link } from 'src/components/common/Link';

import { CollectionT } from 'src/types';

export const LabelList: React.FC<{
  labels: CollectionT[] | undefined;
  className?: string;
  prefix?: string;
}> = ({ labels, className = '', prefix = '' }) => {
  if (!labels || labels.length === 0) return null;

  return (
    <div className={className}>
      {prefix && <span>{prefix}&nbsp;</span>}
      {labels.map((lbl, i) => (
        <React.Fragment key={lbl.id}>
          {i > 0 && <>,&nbsp;</>}
          <Link href={`/labels/${lbl.id}`}>{lbl.name}</Link>
        </React.Fragment>
      ))}
    </div>
  );
};
