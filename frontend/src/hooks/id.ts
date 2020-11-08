import * as React from 'react';

import { useHistory, useParams } from 'react-router-dom';

import { useToasts } from 'react-toast-notifications';

const isValid = (id: string): boolean => /^\d+$/.test(id);

export const useId = (): number | null => {
  const history = useHistory();
  const { addToast } = useToasts();

  const { id } = useParams<{ id: string }>();

  React.useEffect(() => {
    if (id && !isValid(id)) {
      addToast('Invalid ID.', { appearance: 'error' });
      history.push('/404');
    }
  }, [id, addToast, history]);

  return isValid(id) ? parseInt(id) : null;
};
