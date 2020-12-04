import * as React from 'react';
import { Header, SectionHeader } from 'src/components';

export const NotFound: React.FC = () => (
  <>
    <Header />
    <div className="my-8 text-center">
      <SectionHeader>404</SectionHeader>
      <SectionHeader className="mt-4">you are lost ^.~</SectionHeader>
    </div>
  </>
);
