import * as React from 'react';
import tw from 'twin.macro';

import { Icon } from '~/components/common/Icon';

type ISelect = React.FC<{
  children: React.ReactNode;
  value?: string | number | readonly string[];
  onChange?: (arg0: React.FormEvent<HTMLSelectElement>) => void;
  className?: string;
  label?: string;
  name?: string;
}>;

export const Select: ISelect = ({
  children,
  value,
  onChange,
  className,
  label,
  name,
}) => (
  <div className={className} tw="relative flex items-center">
    {label !== null && (
      <label htmlFor={name} tw="flex-none pr-1">
        {label}:
      </label>
    )}
    <select
      css={[
        tw`z-10 flex-1 py-1 pr-4`,
        tw`bg-transparent appearance-none cursor-pointer text-primary-400`,
      ]}
      id={name}
      value={value}
      onChange={onChange}
    >
      {children}
    </select>
    <Icon
      icon="chevron-down-small"
      tw="absolute right-0 flex-none w-4 text-primary-500"
    />
  </div>
);
