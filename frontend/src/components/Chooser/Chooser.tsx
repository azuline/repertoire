import clsx from 'clsx';
import * as React from 'react';
import { SidebarContext } from 'src/contexts';

import { ElementT, ToggleStarFactory } from './Element';
import { JumpToLetter } from './JumpToLetter';
import { VirtualList } from './VirtualList';

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
          active && (isSidebarOpen ? 'xl:bg-background-800' : 'lg:bg-background-800'),
        )}
      >
        <div
          className={clsx(
            'hidden w-full h-24 -mt-24 bg-background-800',
            active && (isSidebarOpen ? 'xl:block' : 'lg:block'),
          )}
        />
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
            ? 'hidden xl:flex xl:flex-col xl:sticky xl:top-0'
            : 'hidden lg:flex lg:flex-col lg:sticky lg:top-0'
          : 'w-full',
      ),
    [className, active, isSidebarOpen],
  );
