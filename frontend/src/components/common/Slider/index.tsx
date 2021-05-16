import React from 'react';
import ReactSlider from 'react-slider';
import tw, { styled } from 'twin.macro';

type ISlider = React.FC<React.ComponentProps<typeof ReactSlider>>;

export const Slider: ISlider = (props) => (
  <Wrapper>
    <ReactSlider className="slider" {...props} />
  </Wrapper>
);

const Wrapper = styled.div`
  ${tw`full`}

  .slider {
    ${tw`flex items-center justify-center full`}

    .track-0 {
      ${tw`cursor-pointer bg-foreground-300`}
    }

    .track-1 {
      ${tw`bg-gray-500 cursor-pointer`}
    }

    .thumb {
      ${tw`
        w-4
        h-4
        cursor-pointer
        bg-primary-400
        rounded-2xl
        leading-4
        hover:(h-6 leading-6 w-6)
      `}
    }
  }
`;
