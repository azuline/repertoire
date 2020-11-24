import * as React from 'react';

import clsx from 'clsx';

export const LoggingIn: React.FC<{ className?: string | undefined }> = ({ className }) => {
  return (
    <div className={clsx(className, 'text-lg flex content-center')}>
      <div className="mx-auto self-center">Logging in...</div>
    </div>
  );
};
