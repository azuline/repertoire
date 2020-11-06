import * as React from 'react';

import clsx from 'clsx';

// Null `element` means it's the "All" select.

export type ElementT = { id: number; name: string };

export const Element: React.FC<{
  element: ElementT | null;
  active: number;
  setActive: (arg0: number) => void;
}> = ({ element, active, setActive }) => {
  const isActive = React.useMemo(
    () => (active === 0 && !element) || (element && element.id === active),
    [active, element],
  );

  // prettier-ignore
  const onClick = React.useCallback(
    () => setActive(element ? element.id : 0),
    [element, setActive],
  );

  return (
    <div
      className={clsx(
        'pl-2 pr-1 py-1 hover:bg-white hover:bg-opacity-5 cursor-pointer truncate',
        isActive ? 'text-bold font-bold' : '',
      )}
      onClick={onClick}
    >
      {element ? element.name : 'All'}
    </div>
  );
};
