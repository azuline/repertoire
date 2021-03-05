import * as React from 'react';
import { AppStyles } from '~/Styles';
import { GlobalStyles } from 'twin.macro';
import { themes } from '@storybook/theming';

export const parameters = {
  actions: { argTypesRegex: '^on[A-Z].*' },
  layout: 'centered',
  docs: {
    theme: themes.dark,
  },
};

export const decorators = [
  (Story) => (
    <>
      <GlobalStyles />
      <AppStyles>
        <Story />
      </AppStyles>
    </>
  ),
];
