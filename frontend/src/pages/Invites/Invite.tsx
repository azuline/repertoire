import * as React from 'react';
import { useToasts } from 'react-toast-notifications';

import { Icon, ListItem } from '~/components';
import { IInvite } from '~/graphql';
import { timeUntil } from '~/util';

const SECONDS_IN_DAY = 24 * 60 * 60;

type IInviteComponent = React.FC<
  Pick<IInvite, 'id' | 'createdAt' | 'code' | 'createdBy'>
>;

export const Invite: IInviteComponent = ({ id, createdAt, code, createdBy }) => {
  const { addToast } = useToasts();

  const expiresAt = new Date((createdAt + SECONDS_IN_DAY) * 1000);

  const copyCode = (): void => {
    const url = `${window.location.protocol}//${window.location.host}/register/${code}`;
    navigator.clipboard.writeText(url);
    addToast('Copied code to clipboard!', { appearance: 'success' });
  };

  return (
    <ListItem key={id} tw="py-2 px-3 flex items-center" onClick={copyCode}>
      <div tw="text-foreground-100 inline-block mr-3">
        <Icon icon="clipboard" tw="w-4 h-4" />
      </div>
      <span tw="text-foreground-400 mr-1.5">Created by</span>
      <span tw="text-foreground-300">{createdBy.nickname}</span>
      <span tw="text-foreground-400 mr-1.5">. Expires in</span>
      <span tw="text-foreground-100">{timeUntil(expiresAt)}</span>
      <span tw="text-foreground-400 mr-3">.</span>
      <div tw="inline-block text-foreground-400 mr-3">
        <Icon icon="arrow-right" tw="w-4 h-4" />
      </div>
      <span tw="text-foreground-400">{code}</span>
    </ListItem>
  );
};
