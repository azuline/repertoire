import * as React from 'react';
import { Icon } from 'src/components/common/Icon';

export const BackButton: React.FC = () => (
  <button type="button" className="-ml-3 flex items-center text-btn large">
    <Icon className="w-5 -ml-2 mr-1" icon="chevron-left-small" />
    <div className="flex-shrink">Back</div>
  </button>
);
