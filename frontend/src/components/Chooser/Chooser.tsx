import clsx from 'clsx';
import * as React from 'react';
import { SidebarContext } from 'src/contexts';

import { ElementT, ToggleStarFactory } from './Element';
import { JumpToLetter } from './JumpToLetter';
import { VirtualList } from './VirtualList';

/**
 * TODO: At the moment, the pages on which this is used essentially have a fixed header. Whereas, on
 * other pages, the header scrolls with the rest of the page.
 *
 * It would be nice if this could use the scroll container of the main application rather than its
 * own scroll container.
 *
 * I have attempted to use the WindowScroller, which worked well with the exception of one problem:
 * the scrollbar extended into the footer.
 *
 * We are going for an application feel, and the scrollbar going into the footer just breaks the
 * feel entirely. So we are settling for the sticky header, **for now**.
 */

export const Chooser: React.FC<{
  className?: string;
  results: ElementT[];
  active: number | null;
  urlFactory: (arg0: number) => string;
  starrable?: boolean;
  toggleStarFactory: ToggleStarFactory;
}> = ({ className, results, active, urlFactory, starrable, toggleStarFactory }) => {
  const { isSidebarOpen } = React.useContext(SidebarContext);
  const [jumpTo, setJumpTo] = React.useState<number | null>(null);

  return (
    <div
      className={clsx(
        className,
        'w-72 -ml-6 md:-ml-8',
        active && 'mr-6 md:mr-8',
        active && isSidebarOpen && 'hidden lg:flex lg:flex-col lg:sticky lg:top-0',
        active && !isSidebarOpen && 'hidden md:flex md:flex-col md:sticky md:top-0',
        !active && '-mr-6 md:-mr-8 w-fullpad',
      )}
      style={{ maxHeight: 'calc(100vh - 4rem)' }}
    >
      <div
        className={clsx(
          'relative flex-auto h-full',
          active &&
            (isSidebarOpen
              ? 'lg:bg-background-800 lg:sticky lg:top-0'
              : 'md:bg-background-800 md:sticky md:top-0'),
        )}
      >
        <JumpToLetter active={active} results={results} setJumpTo={setJumpTo} />
        <VirtualList
          active={active}
          jumpTo={jumpTo}
          results={results}
          starrable={starrable}
          toggleStarFactory={toggleStarFactory}
          urlFactory={urlFactory}
        />
      </div>
    </div>
  );
};
