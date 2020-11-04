import * as React from 'react';

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
    <div className={className}>
      {label && (
        <label htmlFor={id} className="self-center mr-4 text-lg">
          {label}
        </label>
      )}
      <select
        id={id}
        onChange={onChange}
        className="p-2 bg-white leading-tight rounded border-2 border-highlight"
      >
        {children}
      </select>
    </div>
  );
};
