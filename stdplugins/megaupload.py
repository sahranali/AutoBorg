# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

""" command: .megaupload """

from telethon import events
import wikipedia


@borg.on(events.NewMessage(pattern=r".megaupload (.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Processing ...")
    input_str = event.pattern_match.group(1)
    result = wikipedia.summary(input_str)
    await event.edit(".exec curl -F "file=@{}"  https://api.megaupload.is/upload".format(input_str))

