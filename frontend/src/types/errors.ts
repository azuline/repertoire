export class RequestError<T> extends Error {
  errors: T[];

  constructor(message = 'uwu request error', errors: T[] = []) {
    super(message);
    this.errors = errors;
  }
}
