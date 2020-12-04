import clsx from 'clsx';
import * as React from 'react';

export const Popover: React.FC<{
  children: [React.ReactElement, React.ReactElement];
  hover?: boolean;
  click?: boolean;
  className?: string;
}> = ({ children, hover = false, click = false, className }) => {
  const [child1, child2] = children;
  const [open, setOpen] = React.useState<boolean>(false);

  return (
    <div className={clsx(className, hover ? 'hover-popover' : 'popover')}>
      {React.cloneElement(child1, { onClick: (): void => setOpen((o) => !o) })}
      <div className={clsx('relative z-40', open && click && 'block-important')}>
        <div
          className="fixed top-0 left-0 w-screen h-screen"
          onClick={(): void => setOpen(false)}
        />
        <div className="absolute right-1.5 w-3 h-3 mt-2.5 bg-primary-800 transform rotate-45" />
        <div className="absolute right-0 z-10 px-6 py-4 mt-4 border-2 rounded bg-background-800 border-primary-800">
          {child2}
        </div>
      </div>
    </div>
  );
};
