import { ApolloError, gql } from '@apollo/client';
import * as React from 'react';
import { useToasts } from 'react-toast-notifications';

import { Button, Input } from '~/components';
import { useIndexCrontabQuery, useUpdateIndexCrontabMutation } from '~/graphql';

// TODO: Offer a few sane options and then offer a custom crontab option.

export const IndexCrontab: React.FC = () => {
  const [indexCrontab, setIndexCrontab] = React.useState<string>('');
  const { addToast } = useToasts();

  const { data, loading } = useIndexCrontabQuery();
  const [mutateConfig] = useUpdateIndexCrontabMutation();

  React.useEffect(() => data && setIndexCrontab(data.config.indexCrontab), [data]);

  if (data === undefined || loading === true) {
    return <>Loading... do a proper animation later</>;
  }

  const updateIndexCrontab = async (
    event: React.FormEvent<HTMLFormElement>,
  ): Promise<void> => {
    event.preventDefault();

    try {
      await mutateConfig({ variables: { indexCrontab } });
      addToast('Updated indexer crontab.', { appearance: 'success' });
    } catch (e) {
      if (e instanceof ApolloError) {
        addToast(e.message, { appearance: 'error' });
      }
    }
  };

  return (
    <div tw="flex">
      <div>Library Indexer Crontab:</div>
      <form tw="ml-8" onSubmit={updateIndexCrontab}>
        <Input
          placeholder="New directory"
          value={indexCrontab}
          onChange={(e): void => setIndexCrontab(e.target.value)}
        />
        <Button tw="ml-4" type="submit">
          Save
        </Button>
      </form>
    </div>
  );
};

gql`
  query IndexCrontab {
    config {
      __typename
      indexCrontab
    }
  }

  mutation UpdateIndexCrontab($indexCrontab: String!) {
    updateConfig(indexCrontab: $indexCrontab) {
      __typename
      indexCrontab
    }
  }
`;
