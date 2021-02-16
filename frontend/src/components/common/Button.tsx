import tw from 'twin.macro';

const BaseButton = tw.button`
  rounded 
  font-normal
  text-foreground
  bg-primary-700 
  hover:bg-primary-600 
`;

export const Button = tw(BaseButton)`
  px-4 
  py-2
`;

export const SmallButton = tw(BaseButton)`
  px-2
  py-1
`;

export const TextButton = tw(BaseButton)`
  bg-transparent
  hover:bg-black
  hover:bg-opacity-5
  text-primary-400
  dark:hover:bg-white
  dark:hover:bg-opacity-5
`;
