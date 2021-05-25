import * as React from 'react';
import tw from 'twin.macro';

type IPopover = React.FC<{
  children: [React.ReactElement, React.ReactElement];
}>;

export const Popover: IPopover = ({ children }) => {
  const [child1, child2] = children;
  const [open, setOpen] = React.useState<boolean>(false);

  return (
    <div>
      {React.cloneElement(child1, { onClick: (): void => setOpen((o) => !o) })}
      {open && (
        <div tw="relative z-40">
          <SetBackground setOpen={setOpen} />
          <Arrow />
          <PopoverBodyWrapper>{child2}</PopoverBodyWrapper>
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

const Arrow = tw.div`
  absolute
  right-1.5
  w-3
  h-3
  mt-2.5
  bg-primary-800
  transform
  rotate-45
`;

const PopoverBodyWrapper = tw.div`
  absolute
  right-0
  z-10
  px-8
  py-6
  mt-4
  border-2
  rounded
  bg-background-800
  border-primary-800
`;
