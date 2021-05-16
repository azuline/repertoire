import React from 'react';
import { useParams } from 'react-router';

import { FullPageLoading } from '~/components';
import { useRequestJson } from '~/hooks';
import { UnauthenticatedError } from '~/pages/Error';

import { RegisterForm } from './Form';

type IRegister = React.FC<{
  onSuccess?: () => void;
  isFirstRegistration?: boolean;
}>;

export const Register: IRegister = ({ onSuccess, isFirstRegistration = false }) => {
  const requestJson = useRequestJson<{ valid: boolean }>();

  const { code: inviteCode } = useParams<{ code: string }>();
  // Default to assuming the code is valid.
  const [validCode, setValidCode] = React.useState<boolean>(true);
  const [loading, setLoading] = React.useState<boolean>(true);

  const verifyToken = async (): Promise<void> => {
    try {
      const { valid } = await requestJson(
        `/api/register/validate-invite?${new URLSearchParams({ inviteCode })}`,
      );

      if (!valid) {
        setValidCode(false);
      }

      setLoading(false);
    } catch (e) {
      setValidCode(false);
      setLoading(false);
    }
  };

  React.useEffect((): void => {
    if (!isFirstRegistration) {
      verifyToken();
    } else {
      setLoading(false);
    }
  }, []);

  if (loading) {
    return <FullPageLoading />;
  }

  if (!validCode) {
    return <UnauthenticatedError title="Invalid invite code." />;
  }

  return (
    <RegisterForm
      inviteCode={inviteCode}
      isFirstRegistration={isFirstRegistration}
      onSuccess={onSuccess}
    />
  );
};
