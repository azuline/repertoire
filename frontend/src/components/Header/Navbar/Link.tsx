import * as React from 'react';

import { useHistory } from 'react-router-dom';

export const Link: React.FC<{ name: string; url: string }> = ({ name, url }) => {
  const history = useHistory();
  const handleClick = React.useCallback(() => history.push(url), [history, url]);

  return (
    <button
      className="bg-transparent hover:bg-gray-900 font-semibold px-4 mr-2"
      onClick={handleClick}
    >
      {name}
    </button>
  );
};
