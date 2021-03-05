import tw, { styled, TwStyle } from 'twin.macro';

type IProps = {
  small?: boolean;
  text?: boolean;
};

export const Button = styled.button<IProps>`
  ${tw`
    rounded 
    font-normal
    text-foreground
    bg-primary-700 
    hover:bg-primary-600 
  `}

  ${({ small }): TwStyle => (small === true ? tw`px-2 py-1` : tw`px-4 py-2`)}

  ${({ text }): TwStyle | boolean =>
    text === true &&
    tw`
      bg-transparent
      text-primary-400
      hover:(bg-black bg-opacity-5)
      dark:hover:(bg-white bg-opacity-5)
    `}
`;
