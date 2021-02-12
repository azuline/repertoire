module.exports = {
  '*.{js,jsx,ts,tsx}': ['eslint --fix'],
  '*.{json,html,md}': ['prettier --write'],
  '*.{py}': ['black && isort && flake8'],
};
