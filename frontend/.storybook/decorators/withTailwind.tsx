import * as React from 'react';
import 'src/index.css';

export const withTailwind = (story) => <div className="bg-gray-100 p-8">{story()}</div>;
