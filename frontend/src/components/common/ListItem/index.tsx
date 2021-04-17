import * as React from 'react';
import tw from 'twin.macro';

type IListItem = React.FC<{
  className?: string;
  children: React.ReactNode;
  onClick?: () => void;
}>;

export const ListItem: IListItem = ({ className, children, onClick }) => {
  return (
    <div
      className={className}
      css={[tw`rounded`, onClick && tw`cursor-pointer hover-bg`]}
      onClick={onClick}
    >
      {children}
    </div>
  );
};
