import * as React from 'react';
import clsx from 'clsx';
import { defaultTheme } from './Page';
import { Placement } from '@popperjs/core';
import { usePopper } from 'react-popper';
import { useToasts } from 'react-toast-notifications';

// FUCK POPPER.JS DOCS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

export const Skip: React.FC<{
  setCurPage: (arg0: number) => void;
  numPages: number;
  popperPlacement?: Placement;
  className?: string;
}> = ({ setCurPage, numPages, popperPlacement = 'bottom', className = '' }) => {
  const [hidden, setHidden] = React.useState<boolean>(true);
  const [buttonElement, setButtonElement] = React.useState<HTMLButtonElement | null>(null);
  const [popperElement, setPopperElement] = React.useState<HTMLDivElement | null>(null);
  const [arrowElement, setArrowElement] = React.useState<HTMLDivElement | null>(null);
  const { styles, attributes } = usePopper(buttonElement, popperElement, {
    placement: popperPlacement,
    modifiers: [{ name: 'arrow', options: { element: arrowElement } }],
  });

  const toggleHidden = React.useCallback(() => setHidden((h) => !h), [setHidden]);

  const arrowStyles = React.useMemo(() => {
    if (styles && styles.arrow) {
      return {
        ...styles.arrow,
        transform: `${styles.arrow.transform} rotate(45deg) translate(-50%, -50%)`,
      };
    } else {
      return {};
    }
  }, [styles]);

  return (
    <>
      <button
        ref={setButtonElement}
        type="button"
        className={clsx(className, defaultTheme, 'square-btn p-2 border-2 border-gray-400')}
        onClick={toggleHidden}
      >
        &#8230;
      </button>
      {hidden || (
        <div className="z-50" ref={setPopperElement} style={styles.popper} {...attributes.popper}>
          {popperPlacement === 'bottom' && (
            <div className="popper-arrow" ref={setArrowElement} style={arrowStyles} />
          )}
          <PageSelect setCurPage={setCurPage} numPages={numPages} />
          {popperPlacement !== 'bottom' && (
            <div className="popper-arrow" ref={setArrowElement} style={arrowStyles} />
          )}
        </div>
      )}
    </>
  );
};

const PageSelect: React.FC<{
  setCurPage: (arg0: number) => void;
  numPages: number;
}> = ({ setCurPage, numPages }) => {
  const input = React.useRef<HTMLInputElement | null>(null);
  const { addToast } = useToasts();

  const onSubmit = React.useCallback(
    (event) => {
      event.preventDefault();

      if (!input.current) return;

      const page = parseInt(input.current.value);

      if (isNaN(page) || page < 1 || page > numPages) {
        addToast('Invalid page number.', { appearance: 'error' });
        return;
      }

      setCurPage(page);
      input.current.value = '';
    },
    [input],
  );

  return (
    <form className="bg-gray-300 rounded flex p-2" onSubmit={onSubmit}>
      <input className="mr-2" placeholder="Jump to page" ref={input} />
      <button type="submit" className="bg-green-400">
        Go
      </button>
    </form>
  );
};
