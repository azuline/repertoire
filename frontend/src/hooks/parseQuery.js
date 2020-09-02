import { ArtistsContext, CollectionsContext } from 'contexts';
import { useCallback, useContext } from 'react';
import { TopToaster } from 'components/Toaster';
import { unescapeQuotes } from 'common/queries';
import { collectionTypeNamesLowerToIds } from 'common/collections';

const queryRegex = /(artist|system|collage|label|genre):"((?:\\.|[^"\\])*)"/g;

export const useParseQuery = () => {
  const { collections } = useContext(CollectionsContext);
  const { artists } = useContext(ArtistsContext);

  return useCallback(
    (query) => {
      const collectionIds = [];
      const artistIds = [];
      const search = query.replace(queryRegex, '');

      let match;

      while ((match = queryRegex.exec(query))) {
        const [, type, value] = match;
        const unescapedValue = unescapeQuotes(value);

        if (type === 'artist') {
          const artist = artists.find(({ name }) => name === unescapedValue);
          if (!artist) {
            TopToaster.show({
              icon: 'error',
              intent: 'danger',
              message: `${unescapedValue} is not a valid artist.`,
              timeout: 5000,
            });
          } else {
            artistIds.push(artist.id);
          }
        } else {
          const typeId = collectionTypeNamesLowerToIds[type];
          const collection = collections.find(
            ({ type, name }) => type === typeId && name === unescapedValue
          );

          if (!collection) {
            TopToaster.show({
              icon: 'error',
              intent: 'danger',
              message: `${unescapedValue} is not a valid ${type} collection.`,
              timeout: 5000,
            });
          } else {
            collectionIds.push(collection.id);
          }
        }
      }

      return [search, collectionIds, artistIds];
    },
    [artists, collections]
  );
};
