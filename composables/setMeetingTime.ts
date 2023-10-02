// vim:set ts=2 sw=2 et:

export const setMeetingTime = (target, data) => {
  if (!data.meetings || data.meetings.length != 1) {
    console.log('failed to set meeting time: data missing/invalid');
    return;
  }

  data = data.meetings[0];

  if (!target.description) {
    return;
  }

  if (data.meeting_date && data.meeting_time_start && data.meeting_timezone) {
    let date = new Date(
      `${data.meeting_date}T${data.meeting_time_start}Z`
    );
    target.description = target.description.replace(
      "$day", date.toLocaleString(
        'en-US', { "weekday": "long" }
      )
    );
    target.description = target.description.replace(
      "$time", date.toLocaleString(
        'en-US', { "timeStyle": "short", "hour12": false, "timeZone": "UTC" }
      ) + ' ' + data.meeting_timezone
    );
  }

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
    target.description = target.description.replace("$location", place);
  }
}
