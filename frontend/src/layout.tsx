import * as React from 'react';
import tw from 'twin.macro';

type IProps = {
  children: React.ReactNode;
  padY?: boolean;
  padX?: boolean;
  scroll?: boolean;
};

export const Layout: React.FC<IProps> = ({ children, padY, padX, scroll }) => (
  <div
    css={[padX === true && tw`pad-page`, scroll === true && tw`overflow-y-auto`]}
    /* We set relative here to create a new z-index stacking context. */
    tw="full relative"
  >
    <div
      css={[padY === true && tw`py-12`]}
      /* Flexbox makes the heights not collapse IDK. */
      tw="full flex"
    >
      {children}
    </div>
  </div>
);

/* Maybe these will be useful later. Delete once done with refactor if not. */
/* flex */
/* flex-col */
/* min-h-0 */
