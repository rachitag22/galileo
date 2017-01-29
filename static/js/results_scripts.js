var jsonURL = "https://daemon-dash-galileo-rachitag22.c9users.io/return-result";

$.ajax({
    url: jsonURL,
    dataType:'json',
    type: 'post',
    data: yourForm.serialize(),
    success:function(response){
                
        var dp = new DayPilot.Calendar("dp");
        
        // behavior and appearance
        dp.cssClassPrefix = "calendar_white";
        // view
        dp.startDate = "2014-02-24";
        dp.days = 5;
        dp.headerDateFormat = "dddd"; // day of week, long format (e.g. "Monday")
        
        dp.events.list = response;
        dp.init();
    }
});

