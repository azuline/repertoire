import * as React from 'react';

import clsx from 'clsx';

const arrowStyle = {
  borderColor: 'transparent var(--color-primary-alt) var(--color-primary-alt) transparent',
};

export const Popover: React.FC<{
  children: React.ReactNode[];
  hover?: boolean;
  click?: boolean;
  className?: string | undefined;
}> = ({ children, hover = false, click = false, className }) => {
  const [child1, child2] = children;
  const [open, setOpen] = React.useState<boolean>(false);

  const toggleOpen = React.useCallback(() => setOpen((o) => !o), [setOpen]);

  const toggler = React.useMemo(
    () => React.cloneElement(child1 as React.ReactElement, { onClick: toggleOpen }),
    [child1, toggleOpen],
  );

  return (
    <div className={clsx(className, 'popover', hover && 'hover-popover')}>
      {toggler}
      <div className={clsx('relative z-40', open && click && 'block-important')}>
        <div className="absolute right-0 border-10" style={arrowStyle} />
        <div className="absolute right-0 pt-4 z-10">{child2}</div>
      </div>
    </div>
  );
};
