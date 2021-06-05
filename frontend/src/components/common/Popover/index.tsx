import * as React from 'react';
import tw, { styled, TwStyle } from 'twin.macro';

type IPopover = React.FC<{
  children: [React.ReactElement, React.ReactElement];
  arrow?: boolean;
  align: 'right' | 'left';
  /**
   * Use this className prop to style the full popover body, arrow and all.
   * One good use case is to add margin to the popover body.
   */
  className?: string;
}>;

export const Popover: IPopover = ({ className, children, align, arrow = false }) => {
  const [child1, child2] = children;
  const [open, setOpen] = React.useState<boolean>(false);

  return (
    <div>
      {React.cloneElement(child1, { onClick: (): void => setOpen((o) => !o) })}
      {open && (
        <div tw="relative z-40">
          <SetBackground setOpen={setOpen} />
          <div
            className={className}
            css={[align === 'right' && tw`right-0`, align === 'left' && tw`left-0`]}
            tw="absolute"
          >
            {arrow && <Arrow align={align} />}
            <PopoverBodyWrapper align={align} className="popover-body-wrapper">
              {child2}
            </PopoverBodyWrapper>
          </div>
        </div>
      )}
    </div>
  );
};

type ISetBackground = React.FC<{
  setOpen: React.Dispatch<React.SetStateAction<boolean>>;
}>;

const SetBackground: ISetBackground = ({ setOpen }) => (
  <div tw="fixed top-0 left-0 w-screen h-screen" onClick={(): void => setOpen(false)} />
);

type IAlignmentProps = {
  align: React.ComponentProps<IPopover>['align'];
};

const Arrow = styled.div<IAlignmentProps>`
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
const PopoverBodyWrapper = styled.div<IAlignmentProps>`
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
