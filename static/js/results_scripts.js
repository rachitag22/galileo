var jsonURL = "https://daemon-dash-galileo-rachitag22.c9users.io/return-result";

    var dp = new DayPilot.Calendar("dp");

    // behavior and appearance
    dp.cssClassPrefix = "calendar_white";

    // view
    dp.startDate = "2014-02-25";
    dp.days = 5;
    
    dp.headerDateFormat = "dddd"; // day of week, long format (e.g. "Monday")

    // dp.events.list = [{
    //     start: "2016-03-25T00:00:00",
    //     end: "2016-03-27T00:00:00",
    //     id: "1",
    //     text: "Event 1"
    // }, {
    //     start: "2016-03-26T12:00:00",
    //     end: "2016-03-27T00:00:00",
    //     id: "2",
    //     text: "Event 2"
    // }];
    
    dp.events.list = response;

    dp.init();
