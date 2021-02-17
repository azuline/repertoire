import * as React from 'react';
import tw from 'twin.macro';

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
  const [jumpTo, setJumpTo] = React.useState<number | null>(null);

  return (
    <div
      className={className}
      css={[
        tw`w-72 -ml-6 md:-ml-8`,
        active
          ? tw`mr-6 md:mr-8 hidden xl:flex xl:flex-col xl:sticky xl:top-0`
          : tw`-mr-6 md:-mr-8 w-fullpad`,
      ]}
      style={{ maxHeight: 'calc(100vh - 4rem)' }}
    >
      <div
        css={[tw`relative flex-auto h-full`, active && tw`xl:bg-background-800 xl:sticky xl:top-0`]}
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
