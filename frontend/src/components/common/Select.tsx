import clsx from 'clsx';
import * as React from 'react';
import { Icon } from 'src/components/common/Icon';

export const Select: React.FC<{
  children: React.ReactNode;
  value?: string | number | readonly string[];
  onChange?: (arg0: React.FormEvent<HTMLSelectElement>) => void;
  className?: string;
  selectClassName?: string;
  label?: string;
  name?: string;
}> = ({ children, value, onChange, className, selectClassName = '', label, name }) => (
  <div className={clsx(className, 'relative flex items-center')}>
    {label && (
      <label htmlFor={name} className="flex-none pr-1">
        {label}:
      </label>
    )}
    <select
      id={name}
      value={value}
      onChange={onChange}
      className={clsx(
        selectClassName,
        'z-10 flex-1 py-1 pr-4 bg-transparent appearance-none cursor-pointer text-primary-alt',
      )}
    >
      {children}
    </select>
    <Icon
      className="absolute right-0 z-0 flex-none w-4 text-primary-alt"
      icon="chevron-down-small"
    />
  </div>
);
