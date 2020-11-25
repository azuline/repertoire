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
  <div className={clsx(className, 'flex items-center relative')}>
    {label && (
      <label htmlFor={name} className="py-1 flex-none">
        {label}:
      </label>
    )}
    <select
      id={name}
      value={value}
      onChange={onChange}
      className={clsx(
        selectClassName,
        'py-1 bg-transparent leading-tight appearance-none text-primary cursor-pointer pr-4 z-10 flex-1',
      )}
    >
      {children}
    </select>
    <Icon className="w-4 text-primary absolute right-0 z-0 flex-none" icon="chevron-down-small" />
  </div>
);
