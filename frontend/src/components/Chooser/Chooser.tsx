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

const chooserStyle = { maxHeight: 'calc(100vh - 4rem)' };

export const Chooser: React.FC<{
  className?: string;
  results: ElementT[];
  active: number | null;
  urlFactory: (arg0: number) => string;
  toggleStarFactory: ToggleStarFactory;
}> = ({ className, results, active, urlFactory, toggleStarFactory }) => {
  const { isSidebarOpen } = React.useContext(SidebarContext);
  const [jumpTo, setJumpTo] = React.useState<number | null>(null);

  return (
    <div
      className={useChooserStyles(className, active, isSidebarOpen)}
      style={active ? chooserStyle : {}}
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
          toggleStarFactory={toggleStarFactory}
          urlFactory={urlFactory}
        />
      </div>
    </div>
  );
};

const useChooserStyles = (
  className: string | undefined,
  active: number | null,
  isSidebarOpen: boolean,
): string =>
  React.useMemo(
    () =>
      clsx(
        className,
        'w-72',
        active // eslint-disable-line no-nested-ternary
          ? isSidebarOpen
            ? 'hidden lg:flex lg:flex-col lg:sticky lg:top-0'
            : 'hidden md:flex md:flex-col md:sticky md:top-0'
          : 'w-full',
      ),
    [className, active, isSidebarOpen],
  );
