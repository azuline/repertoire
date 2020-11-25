import * as React from 'react';
import { useToasts } from 'react-toast-notifications';
import { Icon } from 'src/components/common';

export const Goto: React.FC<{
  setCurPage: (arg0: number) => void;
  numPages: number;
}> = ({ setCurPage, numPages }) => {
  const input = React.useRef<HTMLInputElement | null>(null);
  const { addToast } = useToasts();

  const onSubmit = React.useCallback(
    (event) => {
      event.preventDefault();
      if (!input.current || !/^\d+$/.test(input.current.value)) return;

      const page = parseInt(input.current.value, 10);

      if (page < 1 || page > numPages) {
        addToast('Invalid page number.', { appearance: 'error' });
        return;
      }

      input.current.value = '';
      setCurPage(page);
    },
    [setCurPage, numPages],
  );

  return (
    <form className="flex" onSubmit={onSubmit}>
      <div className="relative ml-1">
        <input className="w-16 py-1 p-0 pr-7 text-center" placeholder="Go" ref={input} />
        <button
          className="absolute right-0 h-full py-0 pl-1 bg-transparent hover:bg-transparent"
          type="submit"
        >
          <Icon className="w-4 text-primary" icon="right-arrow-small" />
        </button>
      </div>
    </form>
  );
};
