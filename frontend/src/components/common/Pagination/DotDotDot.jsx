import React, { useState, useCallback, useContext } from 'react';
import { PaginationContext } from 'contexts';
import { InputGroup, Popover, Button } from '@blueprintjs/core';

export const DotDotDot = () => {
  const [input, setInput] = useState('');
  const [open, setOpen] = useState(false);
  const { setPage, numPages } = useContext(PaginationContext);

  const goToPage = useCallback(() => {
    const page = parseInt(input);

    // TODO: Perhaps have an error popup?
    if (!page || page < 1 || page > numPages) return;

    setPage(page);
    setOpen(false);
  }, [input, numPages, setPage, setOpen]);

  return (
    <Popover isOpen={open} onInteraction={(state) => setOpen(state)}>
      <Button className="DotDotDot">&#8230;</Button>
      <form className="GoToPageForm" onSubmit={goToPage}>
        <InputGroup
          className="GoToPage"
          placeholder="Page"
          value={input}
          onChange={(event) => setInput(event.target.value)}
        />
        <Button icon="arrow-right" intent="success" onClick={goToPage} />
      </form>
    </Popover>
  );
};
