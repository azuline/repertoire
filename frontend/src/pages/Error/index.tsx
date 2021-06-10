import * as React from 'react';

import { SectionHeader } from '~/components';
import { Layout } from '~/layout';

type IErrorPage = React.FC<{ title: string; errors?: string[] }>;

export const ErrorPage: IErrorPage = ({ title, errors }) => (
  <Layout tw="flex flex-col full justify-center items-center">
    <SectionHeader>{title}</SectionHeader>
    <div tw="mt-4 text-xl">
      {(errors ?? []).map((err, i) => (
        // Who knows what's unique about an error?
        // eslint-disable-next-line react/no-array-index-key
        <div key={i} tw="mb-2">
          {err}
        </div>
      ))}
    </div>
  </Layout>
);

export const NotFound: React.FC = () => (
  <ErrorPage errors={['you are lost ^.~']} title="404" />
);
