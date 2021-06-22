import { gql } from '@apollo/client';
import * as React from 'react';

import { Button, SectionHeader } from '~/components';
import {
  refetchInvitesFetchInvitesQuery,
  useInvitesCreateInviteMutation,
  useInvitesFetchInvitesQuery,
} from '~/graphql';
import { Layout } from '~/layout';

import { Invite } from './Invite';

export const Invites: React.FC = () => {
  const { data } = useInvitesFetchInvitesQuery();
  const invites = data?.invites.results;

  const [createInvite] = useInvitesCreateInviteMutation();
  const createOnClick = (): void => {
    void createInvite({ refetchQueries: [refetchInvitesFetchInvitesQuery()] });
  };

  return (
    <Layout pad scroll>
      <SectionHeader tw="pb-4">Active Invites</SectionHeader>
      <div tw="pb-8 text-foreground-500">Click an invite to copy its invite URL.</div>
      <div tw="flex">
        {invites && (
          <div tw="flex-shrink min-w-0">
            {invites.map((inv) => (
              <Invite key={inv.id} {...inv} />
            ))}
          </div>
        )}
        <div tw="flex-1" />
      </div>
      <div tw="py-10">
        <Button onClick={createOnClick}>Create new invite</Button>
      </div>
    </Layout>
  );
};

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
