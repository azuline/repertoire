export const formatDate = (unixTime) => {
  const date = new Date(unixTime * 1000);

  const year = date.getFullYear();
  const month = date.toLocaleString('default', { month: 'short' });
  const day = date.getDate();
  const hour = date.getHours().toString().padStart(2, '0');
  const minute = date.getMinutes().toString().padStart(2, '0');
  const second = date.getSeconds().toString().padStart(2, '0');

  return `${year} ${month} ${day} ${hour}:${minute}:${second}`;
};
