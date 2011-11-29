// create closure
(function($) {
    // plugin definition
    $.fn.dynamiccollapsible = function(options) {
        debug('dynamic collapsible count: ' + this.size());
        // Extend our default options with those provided.
        // Note that the first arg to extend is an empty object -
        // this is to keep from overriding our "defaults" object.
        var opts = $.extend({}, $.fn.dynamiccollapsible.defaults, options);
        // Our plugin implementation code goes here.
        // iterate and reformat each matched element
        return this.each(function() {
            var $this = $(this);

            $this.append( loaddata(opts.dynamicdata) ).trigger('create');

            debug(opts.dynamicdata);
        });
    };

    // plugin defaults - added as a property on our plugin function
    $.fn.dynamiccollapsible.defaults = {
        foreground: 'red',
        dynamicdata: ''
    };
    
    // private function
    function debug(info) {
        if (window.console && window.console.log)
            window.console.log(info);
    };

    function loaddata(d) {
        
        return $('<div data-role="collapsible-set" data-content-theme="b" data-theme="b"> <div data-role="collapsible"> <h3>Section 1</h3> ddddd</div> </div>');
    }

    //  ...
    // end of closure
})(jQuery);

