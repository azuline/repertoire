import { addDecorator } from '@storybook/react';
import { withToastProvider } from './decorators/withToastProvider';
import { withTailwind } from './decorators/withTailwind';

export const parameters = {
  actions: { argTypesRegex: '^on[A-Z].*' },
};

const decorators = [withToastProvider, withTailwind];

decorators.forEach((dec) => addDecorator(dec));
