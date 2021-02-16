import 'twin.macro';

import * as React from 'react';

import { Header, SectionHeader } from '~/components';

type IComponent = React.FC<{ title: string; errors: string[] }>;

export const ErrorP: IComponent = ({ title, errors }) => (
  <div tw="flex flex-col w-full">
    <Header />
    <div tw="my-8 text-center">
      <SectionHeader>{title}</SectionHeader>
      <div tw="mt-4 text-xl">
        {errors.map((err, i) => (
          <div key={i} tw="mb-2">
            {err}
          </div>
        ))}
      </div>
    </div>
  </div>
);

export const NotFound: React.FC = () => <ErrorP errors={['you are lost ^.~']} title="404" />;
