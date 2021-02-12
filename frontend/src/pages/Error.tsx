import * as React from 'react';

import { Header, SectionHeader } from '~/components';

type IComponent = React.FC<{ title: string; errors: string[] }>;

export const ErrorP: IComponent = ({ title, errors }) => (
  <div className="flex flex-col w-full">
    <Header />
    <div className="my-8 text-center">
      <SectionHeader>{title}</SectionHeader>
      <div className="mt-4 text-xl">
        {errors.map((err, i) => (
          <div key={i} className="mb-2">
            {err}
          </div>
        ))}
      </div>
    </div>
  </div>
);

export const NotFound: React.FC = () => <ErrorP errors={['you are lost ^.~']} title="404" />;
