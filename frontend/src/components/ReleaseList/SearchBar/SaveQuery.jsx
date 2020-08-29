import { Button, InputGroup, Popover } from '@blueprintjs/core';
import React, { useContext, useState } from 'react';

import { SearchContext, QueriesContext } from 'contexts';

export const SaveQuery = () => {
  const { query } = useContext(SearchContext);
  const { saveQuery } = useContext(QueriesContext);
  const [name, setName] = useState('');

  const saveQueryForm = () => saveQuery(query, name);

  return (
    <Popover className="SaveQuery" position="bottom">
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
