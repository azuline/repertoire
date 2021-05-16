import React from 'react';
import { useToasts } from 'react-toast-notifications';

import { Button, Icon, Input } from '~/components/common';

type IGoto = React.FC<{
  setCurPage: (arg0: number) => void;
  numPages: number;
}>;

export const Goto: IGoto = ({ setCurPage, numPages }) => {
  const input = React.useRef<HTMLInputElement | null>(null);
  const { addToast } = useToasts();

  const onSubmit = (event: React.FormEvent<HTMLFormElement>): void => {
    event.preventDefault();
    if (!input.current || !/^\d+$/.test(input.current.value)) {
      return;
    }

    const page = parseInt(input.current.value, 10);

    if (page < 1 || page > numPages) {
      addToast('Invalid page number.', { appearance: 'error' });
      return;
    }

    input.current.value = '';
    setCurPage(page);
  };

  return (
    <form tw="flex" onSubmit={onSubmit}>
      <div tw="relative ml-1">
        <Input ref={input} placeholder="Go" tw="w-16 p-0 py-1 text-center pr-6" />
        <Button text tw="absolute right-0 h-full px-1 py-0" type="submit">
          <Icon icon="right-arrow-small" tw="w-4 text-primary-500" />
        </Button>
      </div>
    </form>
  );
};
