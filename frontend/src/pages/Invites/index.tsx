import { gql } from '@apollo/client';
import * as React from 'react';

import { Button, Header, ListItem, SectionHeader } from '~/components';
import {
  IInvite,
  refetchInvitesFetchInvitesQuery,
  useInvitesCreateInviteMutation,
  useInvitesFetchInvitesQuery,
} from '~/graphql';
import { formatDate } from '~/util';

export const Invites: React.FC = () => {
  const { data } = useInvitesFetchInvitesQuery();
  const invites = data?.invites?.results as IInvite[] | undefined;

  const [createInvite] = useInvitesCreateInviteMutation();
  const createOnClick = (): void => {
    createInvite({ refetchQueries: [refetchInvitesFetchInvitesQuery()] });
  };

  if (invites === undefined) {
    return null;
  }

  return (
    <div tw="flex flex-col w-full">
      <Header />
      <div tw="flex flex-col pt-8 w-full">
        <div tw="pb-8">
          <Button onClick={createOnClick}>Create new invite</Button>
        </div>
        <SectionHeader tw="pb-4">Active Invites</SectionHeader>
        <div tw="flex flex-col w-full">
          {invites.map((inv) => (
            <ListItem key={inv.id} tw="py-2 px-3" onClick={(): void => {}}>
              {formatDate(new Date(inv.createdAt))} {inv.code} {inv.createdBy.nickname}
            </ListItem>
          ))}
        </div>
      </div>
    </div>
  );
};

/* eslint-disable */
gql`
  query InvitesFetchInvites {
    invites(includeExpired: true) {
      total
      results {
        ...InviteFields
      }
    }
  }

  mutation InvitesCreateInvite {
    createInvite {
      ...InviteFields
    }
  }
`;
