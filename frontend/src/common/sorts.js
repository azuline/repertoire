export const random = (one, two) => Math.random() - 0.5;
export const title = (one, two) =>
  one.title.toLowerCase() < two.title.toLowerCase() ? -1 : 1;
export const name = (one, two) =>
  one.name.toLowerCase() < two.name.toLowerCase() ? -1 : 1;
export const year = (one, two) => one.year - two.year;
export const releaseCount = (one, two) => one.numReleases - two.numReleases;
export const recentlyAdded = (one, two) => two.addedOn - one.addedOn;
export const recentlyUpdated = (one, two) => two.lastUpdatedOn - one.lastUpdatedOn;
