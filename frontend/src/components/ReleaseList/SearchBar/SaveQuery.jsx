import { Button, InputGroup, Popover } from '@blueprintjs/core';
import { AuthenticationContext, QueriesContext, SearchContext } from 'contexts';
import React, { useCallback, useContext, useState } from 'react';

export const SaveQuery = () => {
  const [name, setName] = useState('');

  const { query } = useContext(SearchContext);
  const { saveQuery } = useContext(QueriesContext);
  const { token } = useContext(AuthenticationContext);

  const saveQueryForm = useCallback(() => saveQuery(token, query, name), [
    saveQuery,
    token,
    query,
    name,
  ]);

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
