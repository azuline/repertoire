import { Position, Toaster } from '@blueprintjs/core';
import './index.scss';

export const TopToaster = Toaster.create({
  className: 'TopToaster',
  position: Position.TOP,
});
