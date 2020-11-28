import * as React from 'react';
import { useToasts } from 'react-toast-notifications';
import { fetchUser, useMutateUser } from 'src/lib';

export const UserSettings: React.FC = () => {
  const { data } = fetchUser();
  const input = React.useRef<HTMLInputElement>(null);
  const { addToast } = useToasts();

  const onSuccess = React.useCallback(() => {
    addToast('Successfully updated nickname.', { appearance: 'success' });
  }, [addToast]);

  const onError = React.useCallback(() => {
    addToast('Failed to update nickname.', { appearance: 'error' });
  }, [addToast]);

  const [mutate] = useMutateUser({ onSuccess, onError });

  const onSubmit = React.useCallback(
    (event) => {
      event.preventDefault();

      if (!input || !input.current) return;

      mutate({ nickname: input.current.value });
    },
    [mutate, input],
  );

  return (
    <div className="flex items-center my-2">
      <div className="flex-none w-32">Nickname:</div>
      <form className="flex items-center flex-1 max-w-sm" onSubmit={onSubmit}>
        <input className="flex-1 mr-4" ref={input} placeholder={data?.user?.nickname} />
        <button className="flex-none" type="submit">
          Save
        </button>
      </form>
    </div>
  );
};
