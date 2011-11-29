// create closure
(function($) {
    // plugin definition
    $.fn.recoveryplan = function(options) {
        debug('dynamic collapsible count: ' + this.size());
        // Extend our default options with those provided.
        // Note that the first arg to extend is an empty object -
        // this is to keep from overriding our "defaults" object.
        var opts = $.extend({}, $.fn.recoveryplan.defaults, options);
        // Our plugin implementation code goes here.
        // iterate and reformat each matched element
        return this.each(function() {
            var $this = $(this);

            $this.append( loaddata(opts.dynamicdata) ).trigger('create');

            debug(opts.dynamicdata);
        });
    };

    // plugin defaults - added as a property on our plugin function
    $.fn.recoveryplan.defaults = {
        foreground: 'red',
        dynamicdata: ''
    };
    
    // private function
    function debug(info) {
        if (window.console && window.console.log)
            window.console.log(info);
    };

    function loaddata(str) {
        var json = JSON.parse(str);

        for (var key in json)
        {
            
            // for (var cityObj in value2[countryObj])
            // {
            //     //可以用document.write("  " + value2[countryObj][cityObj].item + "<br />");
            //     document.write(cityObj + "  " + value2[countryObj][cityObj]["name"] + "<br />" );   
            // }
        }
        
        var $collapsibleset = $(document.createElement('div')).attr('data-role', 'collapsible-set')
            .attr('data-content-theme', 'b').attr('data-theme', 'b');

        for (var i = 0; i < json['计划'].length; i++)
        {
            var plan = json['计划'][i];
            
            var $h3 = $(document.createElement('h3')).attr('color', 'black').html(plan['日期'][0]);
            var $collapsible = $(document.createElement('div')).attr('data-role', 'collapsible');
            $collapsible.append($h3);
            
            var $ul = $(document.createElement('ul')).attr('data-role', 'listview');
            var $li = $(document.createElement('li')).attr('data-role', 'fieldcontain');
            var $fieldset = $(document.createElement('fieldset')).attr('data-role', 'controlgroup');
            // var $legend = $(document.createElement('legend')).html('项目');
            // $fieldset.append($legend);
            
            for (var j = 0; j < plan['项目'].length; j++)
            {
                var item = plan['项目'][j];
                var $input = $(document.createElement('input')).attr('type', 'checkbox')
                    .attr('id', 'checkbox-'+j);
                var $label = $(document.createElement('label')).attr('for', 'checkbox-'+j)
                    .html(json['锻炼项目'][item['index']]);

                $fieldset.append($input);
                $fieldset.append($label);
            }
            
            $li.append($fieldset);
            $ul.append($li);
            $collapsible.append($ul);
            
            
            $collapsibleset.append($collapsible);
        }

        return $collapsibleset;
    }

    //  ...
    // end of closure
})(jQuery);

