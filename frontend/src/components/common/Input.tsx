import tw, { styled } from 'twin.macro';

export const Input = styled.input`
  ${tw`px-4 py-2 bg-transparent border-b-2 border-primary-700`}

  &::placeholder {
    ${tw`text-foreground-100`}
  }
`;
