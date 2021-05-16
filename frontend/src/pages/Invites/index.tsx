import { gql } from '@apollo/client';
import React from 'react';

import { Button, Header, SectionHeader } from '~/components';
import {
  IInvite,
  refetchInvitesFetchInvitesQuery,
  useInvitesCreateInviteMutation,
  useInvitesFetchInvitesQuery,
} from '~/graphql';

import { Invite } from './Invite';

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
      <div tw="flex flex-col mt-4">
        <SectionHeader tw="pb-4">Active Invites</SectionHeader>
        <div tw="pb-8 text-foreground-400">Click an invite to copy its invite URL.</div>
        <div tw="flex">
          <div tw="flex-shrink">
            {invites.map((inv) => (
              <Invite key={inv.id} {...inv} />
            ))}
          </div>
          <div tw="flex-1" />
        </div>
        <div tw="py-10">
          <Button onClick={createOnClick}>Create new invite</Button>
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
