var dp = new DayPilot.Calendar("dp");

// behavior and appearance
dp.cssClassPrefix = "calendar_white";

// view
var jsonUrl = "https://daemon-dash-galileo-rachitag22.c9users.io/";


dp.startDate = "2016-08-29";
dp.days = 5;

dp.headerDateFormat = "dddd"; // day of week, long format (e.g. "Monday")

dp.events.list = [{
    "id": "5",
    "text": "Calendar Event 5",
    "start": "2014-02-25T10:30:00",
    "end": "2014-02-25T16:30:00"
}, {
    "id": "6",
    "text": "Calendar Event 6",
    "start": "2014-02-24T09:00:00",
    "end": "2014-02-24T14:30:00"
}, {
    "id": "7",
    "text": "Calendar Event 7",
    "start": "2014-02-27T12:00:00",
    "end": "2014-02-27T16:00:00"
}];

dp.init();