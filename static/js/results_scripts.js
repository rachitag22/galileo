var dp = new DayPilot.Calendar("dp");

// behavior and appearance
dp.cssClassPrefix = "calendar_white";
// view
dp.startDate = "2014-02-24";
dp.days = 5;
dp.headerDateFormat = "dddd"; // day of week, long format (e.g. "Monday")



dp.events.list = arrOfSchedule;
dp.init();
