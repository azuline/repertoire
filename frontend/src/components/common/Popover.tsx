import clsx from 'clsx';
import * as React from 'react';

const arrowStyle = {
  borderColor: 'transparent var(--color-primary-alt) var(--color-primary-alt) transparent',
};

export const Popover: React.FC<{
  children: [React.ReactNode, React.ReactNode];
  hover?: boolean;
  click?: boolean;
  className?: string;
}> = ({ children, hover = false, click = false, className }) => {
  const [child1, child2] = children;
  const [open, setOpen] = React.useState<boolean>(false);

  const toggler = React.useMemo(
    () => React.cloneElement(child1 as React.ReactElement, { onClick: () => setOpen((o) => !o) }),
    [child1, setOpen],
  );

  return (
    <div className={clsx(className, 'popover', hover && 'hover-popover')}>
      {toggler}
      <div className={clsx('relative z-40', open && click && 'block-important')}>
        <div className="absolute right-0 border-10" style={arrowStyle} />
        <div className="absolute right-0 z-10 pt-4">{child2}</div>
      </div>
    </div>
  );
};
