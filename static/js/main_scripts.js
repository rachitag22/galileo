$(document).ready(populateSearches);
var allClasses = getClasses();
var allBuildings = getBuildings();

function populateSearches() {
    populateClasses();
    populateBuildings();
}

function populateClasses() {
    $(".class-search").each(function() {
        $(this).autocomplete({
            source: allClasses
        });
    });
}

function populateBuildings() {
    $(".building-search").each(function() {
        $(this).autocomplete({
            source: allBuildings
        });
    });
}

function addClass() {
    var input = "<div class='form-group'><input class='class-search form-control search-autocomplete' type='text'></div>";
    var error = false;
    var errorInput = null;
    $('#class-search-group').find("input").each(function () {
        var inputValue = this.value;
        if (inputValue == "" || !(contains(allClasses, inputValue))) {
            error = true;
            errorInput = this;
        } else {
            errorInput = this;
        }
    });
    
    if (error) {
        $(errorInput).parent().addClass("has-error");
    } else {
        $(errorInput).parent().removeClass("has-error");
        $("#class-search-group").append(input);
        populateClasses();
    }
    
    
}

function contains(a, obj) {
    var i = a.length;
    while (i--) {
       if (a[i] == obj) {
           return true;
       }
    }
    return false;
}

function getClasses() {
    var classes = [
      "CMSC131",
      "AAC122",
      "DDDD129",
      "BSOS083",
      "ENGR400"
    ];
    return classes;
}

function getBuildings() {
    var buildings = [
        "Prince frederick Hall",
        "Carroll Hall",
        "Easton Hall",
        "Cambridge Community"
    ];
    return buildings;
}