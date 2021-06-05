import * as React from 'react';
import tw from 'twin.macro';

import { JumpToLetter } from './JumpToLetter';
import { VirtualList } from './VirtualList';

export { NoChooserOption } from './NoChooserOption';
export * from './types';

type IVirtualListProps = React.ComponentProps<typeof VirtualList>;

type IChooser = React.FC<{
  className?: string;
  results: IVirtualListProps['results'];
  active: IVirtualListProps['active'];
  renderElement: IVirtualListProps['renderElement'];
}>;

export const Chooser: IChooser = ({ className, results, active, renderElement }) => {
  const [jumpTo, setJumpTo] = React.useState<number | null>(null);

  return (
    <div
      className={className}
      css={[
        tw`w-72`,
        active !== null
          ? tw`mr-6 md:mr-8 hidden xl:flex xl:flex-col xl:sticky xl:top-0`
          : tw`w-full`,
      ]}
    >
      <div
        css={[
          tw`relative flex-auto h-full`,
          active !== null && tw`xl:bg-background-800 xl:sticky xl:top-0`,
        ]}
      >
        <JumpToLetter active={active} results={results} setJumpTo={setJumpTo} />
        <VirtualList
          active={active}
          jumpTo={jumpTo}
          renderElement={renderElement}
          results={results}
        />
      </div>
    </div>
  );
};
