// vim:set ts=2 sw=2 et:

export const getMeetingTime = async (calendar) => {
  const fedocal_api = 'https://calendar.fedoraproject.org/api';

  // figure out the start and end dates for the current week (YYYY-MM-DD)
  const ms_per_day = 86400000; // https://www.w3schools.com/js/js_dates.asp
  const now = Math.floor(Date.now() / ms_per_day); // days since unix epoch
  const dow = new Date().getUTCDay(); // current day of week (0-6; 0=Sunday)
  const sow = now - dow; // start of week
  const eow = sow + 6; // end of week
  const start = new Date(sow * ms_per_day).toISOString().substr(0, 10);
  const end = new Date(eow * ms_per_day).toISOString().substr(0, 10);

  return await $fetch(
    `${fedocal_api}/meetings` +
    `?calendar=${calendar}` +
    `&start=${start}` +
    `&end=${end}`
  );
}
