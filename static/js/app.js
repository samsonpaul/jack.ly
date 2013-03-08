$(function(){
  locationChecker.init()
  })

function updateLocation(json) {
    if (json) {
        var el = $('#location').empty()
        el.removeClass('highlight')
        var location = json['location']
        var url = 'https://maps.google.com/maps?q=' + location
        var date = moment.utc(json['date']).fromNow()

        var link = '<a href="' + url + '">' + location + '</a>'
        var html = "The last time I was seen active at a computer was in " + link + " about " + date + "."

        el.append(html)
    }
}

var locationChecker = {
    init: function(){
        // We fake a delay otherwise it doesn't seem as fancy.
        if (window.location.pathname === '/') {
            setTimeout(this.makeRequest, 2000)
        } else {
            setTimeout(this.makeRequest, 1000)
        }
        this.ping()
    },

    makeRequest: function(){
        var getResponse = function(json){
            if (json) {
                updateLocation(json)
            }
        }
$.getJSON('http://computer-location.herokuapp.com/current-location', getResponse)
    },


    ping: function(){
        setTimeout(function(){locationChecker.init()}, 10000)
    }
}
