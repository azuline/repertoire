import { SerializedStyles } from '@emotion/react';
import * as React from 'react';
import tw, { css, styled, TwStyle } from 'twin.macro';

type IPopover = React.FC<{
  children: [React.ReactElement, React.ReactElement];

  /**
   * How to align the popover body with the trigger elmeent.
   */
  align: 'right' | 'left';

  /**
   * Whether to include an arrow at the top of the popover.
   */
  arrow?: boolean;

  /**
   * Use this className prop to style the full popover body, arrow and all.
   * One good use case is to add margin to the popover body.
   */
  className?: string;

  /**
   * Whether to also display the popover body when the trigger element is hovered on.
   */
  hover?: boolean;
}>;

export const Popover: IPopover = ({
  className,
  children,
  align,
  arrow = false,
  hover = false,
}) => {
  const [child1, child2] = children;
  const [open, setOpen] = React.useState<boolean>(false);

  return (
    <Wrapper hover={hover}>
      {React.cloneElement(child1, { onClick: (): void => setOpen((o) => !o) })}
      <div className={open ? 'open' : ''} tw="relative z-40">
        {open && <SetBackground setOpen={setOpen} />}
        <div
          className={className}
          css={[align === 'right' && tw`right-0`, align === 'left' && tw`left-0`]}
          tw="absolute"
        >
          {arrow && <Arrow align={align} />}
          <PopoverBody align={align} className="popover-body-wrapper">
            {child2}
          </PopoverBody>
        </div>
      </div>
    </Wrapper>
  );
};

const Wrapper = styled.div<{ hover: boolean }>`
  & > :nth-child(2) {
    display: none;
  }
  & > .open {
    display: block;
  }
  ${({ hover }): SerializedStyles | boolean =>
    hover &&
    css`
      &:hover > :nth-child(2) {
        display: block;
      }
    `}
`;

type ISetBackground = React.FC<{
  setOpen: React.Dispatch<React.SetStateAction<boolean>>;
}>;

const SetBackground: ISetBackground = ({ setOpen }) => (
  <div tw="fixed top-0 left-0 w-screen h-screen" onClick={(): void => setOpen(false)} />
);

const Arrow = styled.div<{ align: React.ComponentProps<IPopover>['align'] }>`
  ${tw`
    absolute
    w-3
    h-3
    bg-background-950
    transform
    rotate-45
  `}

  ${({ align }): TwStyle | boolean => align === 'right' && tw`right-1.5`}
  ${({ align }): TwStyle | boolean => align === 'left' && tw`left-1.5`}
`;

// TODO: Drop shadow.
const PopoverBody = styled.div<{ align: React.ComponentProps<IPopover>['align'] }>`
  ${tw`
    absolute
    z-20
    mt-1.5
    border-2
    rounded
    bg-background-900
    border-background-950
  `}

  ${({ align }): TwStyle | boolean => align === 'right' && tw`right-0`}
  ${({ align }): TwStyle | boolean => align === 'left' && tw`left-0`}
`;
