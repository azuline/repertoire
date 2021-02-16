import tw, { styled } from 'twin.macro';

/* TODO: Make the transitions like... work. */

export const TwoSided = styled.div`
  transition: all 0.4s;

  &:hover > :first-child {
    ${tw`hidden w-0 h-0`}
  }

  &:not(:hover) > :nth-child(2) {
    ${tw`hidden w-0 h-0`}
  }
`;
