import * as React from 'react';
import { Link } from 'src/components/common/Link';
import clsx from 'clsx';
import { TitleContext } from 'src/contexts';

export const Title: React.FC<{ className?: string }> = ({ className = '' }) => {
  const { titles } = React.useContext(TitleContext);

  return (
    <div className={clsx(className, 'text-sm uppercase')}>
      <Link className="text-bold" href="/">
        repertoire
      </Link>
      {titles.map(({ label, url }, i) => (
        <React.Fragment key={i}>
          <span className="mx-1">&gt;&gt;=</span>
          <Link href={url} className="text-bold">
            {label}
          </Link>
        </React.Fragment>
      ))}
    </div>
  );
};
