import * as React from 'react';
import clsx from 'clsx';
import { Icon } from 'src/components/common/Icon';

let id = 0;
const newId = (): string => `select-${id++}`;

export const Select: React.FC<{
  children: React.ReactNode;
  onChange?: (arg0: React.FormEvent<HTMLSelectElement>) => void | undefined;
  className?: string;
  label?: string | undefined;
}> = ({ children, onChange = undefined, className = '', label = undefined }) => {
  const id = React.useMemo(newId, []);

  return (
    <div className={clsx(className, 'flex items-center relative')}>
      {label && (
        <label htmlFor={id} className="py-1">
          {label}:
        </label>
      )}
      <select
        id={id}
        onChange={onChange}
        className="py-1 bg-transparent leading-tight appearance-none text-gold-500 cursor-pointer pr-4"
      >
        {children}
      </select>
      <Icon className="w-4 text-gold-500 absolute right-0" icon="chevron" />
    </div>
  );
};
