import * as React from 'react';
import { useToasts } from 'react-toast-notifications';
import { Icon } from 'src/components/common';

export const Goto: React.FC<{
  setCurPage: (arg0: number) => void;
  numPages: number;
}> = ({ setCurPage, numPages }) => {
  const input = React.useRef<HTMLInputElement | null>(null);
  const { addToast } = useToasts();

  const onSubmit = (event: React.FormEvent<HTMLFormElement>): void => {
    event.preventDefault();
    if (!input.current || !/^\d+$/.test(input.current.value)) return;

    const page = parseInt(input.current.value, 10);

    if (page < 1 || page > numPages) {
      addToast('Invalid page number.', { appearance: 'error' });
      return;
    }

    input.current.value = '';
    setCurPage(page);
  };

  return (
    <form className="flex" onSubmit={onSubmit}>
      <div className="relative ml-1">
        <input ref={input} className="w-16 p-0 py-1 text-center pr-7" placeholder="Go" />
        <button className="absolute right-0 h-full py-0 pl-1 pr-2 text-btn" type="submit">
          <Icon className="w-4 text-primary-500" icon="right-arrow-small" />
        </button>
      </div>
    </form>
  );
};
