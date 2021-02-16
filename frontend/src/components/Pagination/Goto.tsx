import * as React from 'react';
import { useToasts } from 'react-toast-notifications';

import { Icon, Input, TextButton } from '~/components/common';

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
        <Input ref={input} className="w-16 p-0 py-1 text-center pr-6" placeholder="Go" />
        <TextButton className="absolute right-0 h-full px-1 py-0" type="submit">
          <Icon className="w-4 text-primary-500" icon="right-arrow-small" />
        </TextButton>
      </div>
    </form>
  );
};
