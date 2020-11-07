import * as React from 'react';
import { useToasts } from 'react-toast-notifications';
import { useHistory, useParams } from 'react-router-dom';

export const Release: React.FC = () => {
  const history = useHistory();
  const { id } = useParams<{ id: string }>();
  const { addToast } = useToasts();

  const intId = React.useMemo(() => parseInt(id), [id]);

  React.useEffect(() => {
    if (!/^\d+$/.test(id)) {
      addToast('Invalid release id.', { appearance: 'error' });
      history.push('/404');
    }
  }, [id, addToast, history]);

  return <div>You are viewing release {intId}.</div>;
};
