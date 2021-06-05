import * as React from 'react';
import tw from 'twin.macro';

type IProps = {
  className?: string;
  children: React.ReactNode;
  pad?: boolean;
  scroll?: boolean;
};

export const Layout: React.FC<IProps> = ({
  className,
  children,
  pad = false,
  scroll = false,
}) => (
  <div
    css={[pad && tw`pad-page`, scroll && tw`overflow-y-auto`]}
    /* We set relative here to create a new z-index stacking context. */
    tw="full relative"
  >
    <div className={className} css={[pad && tw`pt-12`]} tw="full">
      {children}
      {pad && (
        /* This is because bottom padding collapses in scroll... */
        <div tw="h-12" />
      )}
    </div>
  </div>
);

/* Maybe these will be useful later. Delete once done with refactor if not. */
/* flex */
/* flex-col */
/* min-h-0 */
