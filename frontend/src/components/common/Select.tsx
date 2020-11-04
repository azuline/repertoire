import * as React from 'react';
import clsx from 'clsx';
import { Icon } from 'src/components/common/Icon';

export const Select: React.FC<{
  children: React.ReactNode;
  onChange?: (arg0: React.FormEvent<HTMLSelectElement>) => void | undefined;
  className?: string;
  label?: string | undefined;
  name?: string | undefined;
}> = ({ children, onChange, className = '', label, name }) => {
  return (
    <div className={clsx(className, 'flex items-center relative')}>
      {label && (
        <label htmlFor={name} className="py-1">
          {label}:
        </label>
      )}
      <select
        id={name}
        onChange={onChange}
        className="py-1 bg-transparent leading-tight appearance-none text-gold-500 cursor-pointer pr-4 z-10"
      >
        {children}
      </select>
      <Icon className="w-4 text-gold-500 absolute right-0 z-0" icon="chevron" />
    </div>
  );
};
