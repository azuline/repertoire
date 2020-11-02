import * as React from 'react';
import clsx from 'clsx';
import { defaultTheme } from './Page';
import { Placement } from '@popperjs/core';
import { usePopper } from 'react-popper';

export const Skip: React.FC<{
  setCurPage: (arg0: number) => void;
  numPages: number;
  popperPlacement?: Placement;
  className?: string;
}> = ({ setCurPage, numPages, popperPlacement = 'bottom', className = '' }) => {
  const [buttonElement, setButtonElement] = React.useState<HTMLButtonElement | null>(null);
  const [popperElement, setPopperElement] = React.useState<HTMLDivElement | null>(null);
  const [arrowElement, setArrowElement] = React.useState<HTMLDivElement | null>(null);
  const { styles, attributes } = usePopper(buttonElement, popperElement, {
    placement: popperPlacement,
    modifiers: [{ name: 'arrow', options: { element: arrowElement } }],
  });

  return (
    <>
      <button
        ref={setButtonElement}
        className={clsx(className, defaultTheme, 'square-btn p-2 border-1')}
      >
        &#8230;
      </button>
      <div ref={setPopperElement} style={styles.popper} {...attributes.popper}>
        <div ref={setArrowElement} style={styles.arrow} />
        <PageSelect setCurPage={setCurPage} numPages={numPages} />
      </div>
    </>
  );
};

const PageSelect: React.FC<{
  setCurPage: (arg0: number) => void;
  numPages: number;
}> = ({ setCurPage, numPages }) => {
  return <div>Hello!</div>;
};
