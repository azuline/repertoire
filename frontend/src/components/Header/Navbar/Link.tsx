import * as React from 'react';
import { useHistory } from 'react-router-dom';

export const Link: React.FC<{ name: string; url: string }> = ({ name, url }) => {
  const history = useHistory();
  const handleClick = React.useCallback(() => history.push(url), [history, url]);

  return (
    <button
      className="bg-transparent font-semibold px-4 hover:bg-gray-300 mr-2"
      onClick={handleClick}
    >
      {name}
    </button>
  );
};
