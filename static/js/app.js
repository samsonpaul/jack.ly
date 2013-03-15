(function(){

String.prototype.substitute = function(object, regexp){
    return String(this).replace(regexp || (/\\?\{([^{}]+)\}/g), function(match, name){
        if (match.charAt(0) == '\\') return match.slice(1);
        return (object[name] != null) ? object[name] : '';
    });
};

})();

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

        loc_data = {'location': location, 'url': url, 'date': date}

        var html = "The last time I was seen active at a computer was in <a href=\"{url}\">{location}</a> about {date}.".substitute(loc_data)

        el.append(html)
    }
}

var locationChecker = {
    init: function(){
        // We fake a delay otherwise it doesn't seem as fancy.
        if (window.location.pathname === '/') {
            setTimeout(this.makeRequest, 2000)
        } else {
            this.makeRequest();
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
