export const collectionQueryFormats = {
  1: (name) => `system:"${name}"`,
  2: (name) => `collage:"${name}"`,
  3: (name) => `label:"${name}"`,
  4: (name) => `genre:"${name}"`,
};

export const escapeQuotes = (string) => {
  return string.replace(/"/g, '\\"');
};

export const unescapeQuotes = (string) => {
  return string.replace(/\\"/g, '"');
};
