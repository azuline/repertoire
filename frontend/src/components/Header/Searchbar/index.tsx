import * as React from 'react';
import clsx from 'clsx';
import { Icon } from 'src/components/common/Icon';

export const Searchbar: React.FC<{ className?: string }> = ({ className }) => {
  return <Icon icon="search-medium" className={clsx(className, 'w-6 text-bold')} />;
};
