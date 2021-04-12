import { gql } from '@apollo/client';
import * as React from 'react';

import { Button, Header } from '~/components';
import {
  IInvite,
  useInvitesCreateInviteMutation,
  useInvitesFetchInvitesQuery,
} from '~/graphql';

export const Invites: React.FC = () => {
  const { data } = useInvitesFetchInvitesQuery();
  const invites = data?.invites?.results as IInvite[] | undefined;

  const [createInvite] = useInvitesCreateInviteMutation();
  const createOnClick = (): void => {
    createInvite();
  };

  if (invites === undefined) {
    return null;
  }

  return (
    <div tw="flex flex-col w-full">
      <Header />
      <div tw="flex w-full">
        <div>
          <Button onClick={createOnClick}>Create Invite</Button>
        </div>
        <div tw="flex flex-col w-full">
          {invites.map((inv) => (
            <div key={inv.id}>
              {inv.id} {inv.code} {inv.createdBy.nickname}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

/* eslint-disable */
gql`
  query InvitesFetchInvites {
    invites {
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
