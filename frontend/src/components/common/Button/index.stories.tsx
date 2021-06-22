import type { Meta, Story } from '@storybook/react';
import * as React from 'react';

import { Button } from './index';

export default {
  component: Button,
  parameters: {
    docs: {
      description: {
        component: 'A button for clicking on.',
      },
    },
  },
  title: 'Porcelain/Button',
} as Meta;

type IButtonProps = React.ComponentProps<typeof Button> & { as?: string };

const Template: Story<IButtonProps> = (props) => <Button {...props} />;

export const Default = Template.bind({});
Default.args = {
  children: 'Click Me',
  // eslint-disable-next-line no-alert
  onClick: (): void => alert('clicked!'),
};

export const Small = Template.bind({});
Small.args = {
  ...Default.args,
  small: true,
};

export const Text = Template.bind({});
Text.args = {
  ...Default.args,
  text: true,
};

export const SmallText = Template.bind({});
SmallText.args = {
  ...Default.args,
  small: true,
  text: true,
};
