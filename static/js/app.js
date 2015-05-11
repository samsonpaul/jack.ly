// jshint eqnull:true
(function(){ 'use strict';

if (!String.prototype.substitute) {
    String.prototype.substitute = function(object, regexp){
        return String(this).replace(regexp || (/\\?\{([^{}]+)\}/g), function(match, name){
            if (match.charAt(0) == '\\') return match.slice(1);
            return (object[name] != null) ? object[name] : '';
        });
    };
}

var locationChecker = {
    init: function(){
        // We fake a delay otherwise it doesn't seem as fancy.
        if (window.location.pathname === '/')
            setTimeout(locationChecker.makeRequest, 2000);
        else
            locationChecker.makeRequest();

        locationChecker.ping();
    },

    makeRequest: function(){
        $.getJSON('http://computer-location.herokuapp.com/current-location', locationChecker.getResponse);
    },

    getResponse: function(json){
        if (!json) return;
        locationChecker.updateLocation(json);
    },

    ping: function(){
        setTimeout(function(){
            locationChecker.init();
        }, 10000);
    },

    updateLocation: function(json){
        if (!json) return;
        var tmpl = 'The last time I was seen active at a computer was in <a href = \"{url}\">{location}</a> about {date}.',
            el   = $('#location').empty().removeClass('highlight');

        el.append(tmpl.substitute({
            'location' : json.location,
            'url'      : 'https://maps.google.com/maps?q=' + json.location,
            'date'     : window.moment.utc(json.date).fromNow()
        }));
    }
};

$(function(){
    // locationChecker.init();
});

})();
