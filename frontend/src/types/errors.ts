export class RequestError<T> extends Error {
  errors: T[];

  constructor(message = 'uwu request error', errors: T[] = []) {
    super(message);
    this.errors = errors;
  }
}

export type GraphQLError = {
  type: string;
  message: string;
  locations: { line: number; column: number }[];
  path: string[];
};
