import type { Meta, Story } from '@storybook/react';
import React from 'react';

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
  onClick: (): void => alert('clicked!'), // eslint-disable-line no-alert
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
