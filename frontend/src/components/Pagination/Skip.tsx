import * as React from 'react';
import clsx from 'clsx';
import { useToasts } from 'react-toast-notifications';
import { Popover } from 'src/components/common/Popover';

export const Skip: React.FC<{
  setCurPage: (arg0: number) => void;
  numPages: number;
  popperPlacement?: string;
  className?: string;
}> = ({ setCurPage, numPages, popperPlacement = 'bottom-center', className = '' }) => {
  return (
    <Popover placement={popperPlacement} arrowColor="text-gray-300">
      <button
        className={clsx(
          className,
          'square-btn p-2 rounded-none border-2 border-l-0 border-gray-400',
        )}
      >
        &#8230;
      </button>
      <PageSelect setCurPage={setCurPage} numPages={numPages} />
    </Popover>
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

      input.current.value = '';
      setCurPage(page);
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
