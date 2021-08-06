import { ApolloError, gql } from '@apollo/client';
import * as React from 'react';
import { useToasts } from 'react-toast-notifications';

import { Icon, Input } from '~/components';
import { useMusicDirectoriesQuery, useUpdateMusicDirectoriesMutation } from '~/graphql';

export const MusicDirectories: React.FC = () => {
  const [newDirectory, setNewDirectory] = React.useState<string>('');
  const { addToast } = useToasts();

  const { data, loading } = useMusicDirectoriesQuery();
  const [mutateConfig] = useUpdateMusicDirectoriesMutation();

  if (data === undefined || loading === true) {
    // TODO: Animation.
    return <>Loading... do a proper animation later</>;
  }

  const { musicDirectories } = data.config;

  const addNewDirectory = async (): Promise<void> => {
    const oldDirectories = musicDirectories.map((md) => md.directory);
    try {
      await mutateConfig({
        variables: { musicDirectories: [...oldDirectories, newDirectory] },
      });

      setNewDirectory('');
    } catch (e) {
      if (e instanceof ApolloError) {
        addToast(e.message, { appearance: 'error' });
      }
    }
  };

  const removeDirectory = async (directory: string): Promise<void> => {
    // TODO: this isn't replacing cache for some reason IDK.
    try {
      await mutateConfig({
        variables: {
          musicDirectories: musicDirectories
            .map((md) => md.directory)
            .filter((d) => d !== directory),
        },
      });
    } catch (e) {
      if (e instanceof ApolloError) {
        addToast(e.message, { appearance: 'error' });
      }
    }
  };

  return (
    <div tw="flex">
      <div>Music Library Directories:</div>
      <div tw="ml-8 flex flex-col gap-2">
        {musicDirectories.map((md, idx) => (
          // Can have duplicates...
          // eslint-disable-next-line react/no-array-index-key
          <div key={idx} tw="py-1 px-4">
            <div tw="flex items-center gap-2">
              <div>{md.directory}</div>
              <div>{md.existsOnDisk || "Doesn't exist on Disk! Style this later"}</div>
              <div
                tw="px-1 py-2 cursor-pointer hover-bg flex items-center text-primary-400 rounded gap-1"
                onClick={(): Promise<void> => removeDirectory(md.directory)}
              >
                <Icon icon="minus-small" tw="w-5" />
                <div>Remove</div>
              </div>
            </div>
          </div>
        ))}
        <div tw="flex items-center gap-2">
          <Input
            placeholder="New directory"
            value={newDirectory}
            onChange={(e): void => setNewDirectory(e.target.value)}
          />
          <div
            tw="px-1 py-2 cursor-pointer hover-bg flex items-center text-primary-400 rounded gap-1"
            onClick={addNewDirectory}
          >
            <Icon icon="plus-small" tw="w-5" />
            <div>Add</div>
          </div>
        </div>
      </div>
    </div>
  );
};

gql`
  query MusicDirectories {
    config {
      __typename
      musicDirectories {
        directory
        existsOnDisk
      }
    }
  }

  mutation UpdateMusicDirectories($musicDirectories: [String!]) {
    updateConfig(musicDirectories: $musicDirectories) {
      __typename
      musicDirectories {
        directory
        existsOnDisk
      }
    }
  }
`;
