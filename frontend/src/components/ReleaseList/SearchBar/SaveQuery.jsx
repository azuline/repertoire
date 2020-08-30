import { QueriesContext, SearchContext } from 'contexts';
import { Button, InputGroup, Popover } from '@blueprintjs/core';
import React, { useCallback, useContext, useState } from 'react';
import { TopToaster } from 'components/Toaster';

export const SaveQuery = () => {
  const [name, setName] = useState('');
  const [open, setOpen] = useState(false);
  const { query } = useContext(SearchContext);
  const { saveQuery } = useContext(QueriesContext);

  const saveQueryForm = useCallback(() => {
    saveQuery(name, query);
    setOpen(false);
    TopToaster.show({
      icon: 'search',
      intent: 'success',
      message: 'Query saved!',
      timeout: 2000,
    });
  }, [saveQuery, setOpen, query, name]);

  return (
    <Popover
      className="SaveQuery"
      position="bottom"
      isOpen={open}
      onInteraction={(state) => setOpen(state)}
    >
      <Button minimal text="Save" className="SaveButton" />
      <form className="SaveForm" onSubmit={saveQueryForm}>
        <InputGroup
          className="SaveName"
          placeholder="Name"
          value={name}
          onChange={(event) => setName(event.target.value)}
        />
        <Button icon="arrow-right" intent="success" onClick={saveQueryForm} />
      </form>
    </Popover>
  );
};
