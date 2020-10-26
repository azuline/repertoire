import * as React from 'react';
import clsx from 'clsx';
import { PaginationContext } from 'src/contexts';
import { defaultTheme } from './Page';
import { Popover, PopoverPosition } from 'react-tiny-popover';

export const Skip: React.FC<{
  position?: PopoverPosition;
  className?: string;
}> = ({ position = 'bottom', className = '' }) => {
  const [isOpen, setIsOpen] = React.useState(false);

  const onClick = React.useCallback(() => setIsOpen((o) => !o), [setIsOpen]);

  return (
    <Popover isOpen={isOpen} positions={[position]} content={<PageSelect />}>
      <button
        className={clsx(className, defaultTheme, 'p-2 border-1')}
        onClick={onClick}
      >
        &#8230;
      </button>
    </Popover>
  );
};

const PageSelect: React.FC = () => {
  const { setCurPage, numPages } = React.useContext(PaginationContext);
  return <div>Hello!</div>;
};
