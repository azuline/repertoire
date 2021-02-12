import * as React from 'react';
import { useToasts } from 'react-toast-notifications';

import { useFetchUserQuery, useUpdateUserMutation } from '~/graphql';

export const UserSettings: React.FC = () => {
  const { data } = useFetchUserQuery();
  const input = React.useRef<HTMLInputElement>(null);
  const { addToast } = useToasts();

  const onCompleted = (): void => {
    addToast('Successfully updated nickname.', { appearance: 'success' });
  };

  const [mutateUser] = useUpdateUserMutation({ onCompleted });

  const onSubmit = (event: React.FormEvent<HTMLFormElement>): void => {
    event.preventDefault();

    if (!input || !input.current) return;

    mutateUser({ variables: { nickname: input.current.value } });
  };

  return (
    <div className="flex items-center min-w-0 my-2">
      <div className="flex-none w-28">Nickname:</div>
      <form className="flex items-center flex-1 max-w-sm min-w-0" onSubmit={onSubmit}>
        <input ref={input} className="flex-1 min-w-0 mr-4" placeholder={data?.user?.nickname} />
        <button className="flex-none" type="submit">
          Save
        </button>
      </form>
    </div>
  );
};
