// vim:set ts=2 sw=2 et:

export const setMeetingTime = (target, data) => {
  const { d, t } = useI18n();

  if (!target.description) {
    return;
  }

  let count = data.meetings?.length;
  if (!(count > 0 && count <= 3)) {
    console.log('failed to set meeting time: data missing/invalid');
    return;
  }

  // use the times from the first meeting and discard the rest.
  data = data.meetings[0];

  let _cadence = '$cadence';
  let _time = '$time';
  if (data.meeting_date && data.meeting_time_start && data.meeting_timezone) {
    let date = new Date(
      `${data.meeting_date}T${data.meeting_time_start}Z`
    );
    let day = date.toLocaleString('en-US', { "weekday": "long" }).toLowerCase();
    // bi-weekly meetings are signaled by providing fewer than three meetings
    // in the original data set.
    _cadence = (count == 3) ? t('every_' + day) : t('every_other_' + day);
    _time = d(date, { "timeStyle": "short", "hour12": false, "timeZone": "UTC" });
  }

  let _location = '$location';
  if (data.meeting_location) {
    let match;
    let place = data.meeting_location;
    if (match = /^fedora-meeting(-[1-3])?/.exec(place)) {
      // convert "fedora-meeting(-N)" to a markdown link
      // to the appropriate matrix chat room
      let room = `#${match[0].substr(7)}:fedoraproject.org`;
      let text = room.replace(":", "\u200B:");
      let link = `https://chat.fedoraproject.org/#/room/${room}`;
      place = `[${text}](${link})`;
    } else if (match = /^#.*:fedoraproject.org$/.exec(place)) {
      // convert "#<whatever>:fedoraproject.org" to a markdown link
      // to the appropriate matrix chat room
      let text = match[0].replace(":", "\u200B:");
      let link = `https://chat.fedoraproject.org/#/room/${match[0]}`;
      place = `[${text}](${link})`;
    } else if (match = /^https:\/\/(.*)$/.exec(place)) {
      // add zero-width-space chars to the link text to allow wrapping
      let text = "https://" + match[1].replaceAll("/", "\u200B/");
      let link = match[0];
      place = `[${text}](${link})`;
    } else {
      // https://stackoverflow.com/a/59700714 (CC BY-SA 4.0)
      place = place.replace("@", "\u200B[]()@");
    }
    _location = place;
  }

  target.description = t(target.description, { cadence: _cadence, time: _time, location: _location });
}
