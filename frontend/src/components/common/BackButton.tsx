import * as React from 'react';
import { Icon } from 'src/components/common/Icon';

export const BackButton: React.FC = () => (
  <button type="button" className="flex items-center -ml-3 text-btn large">
    <Icon className="w-5 mr-1 -ml-2" icon="chevron-left-small" />
    <div className="flex-shrink">Back</div>
  </button>
);
