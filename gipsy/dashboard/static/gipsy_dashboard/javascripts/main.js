/*globals jQuery, window, document */
(function ($, window, document) {
    "use strict";
    window.REVSQUARE = window.REVSQUARE || {
        $body: null,
        init: function () {
            this.$body = $('body');
            this.moduleToggle();
            this.dropdownArrowToggler();
            this.drawChart();
        },
        drawChart: function () {
            if(!$('.traffic-overview .panel-body').length){
                return;
            }
            $('.traffic-overview .panel-body').highcharts({
                title: false,
                chart: {
                    backgroundColor: "#6098d1"
                },
                xAxis: {
                    categories: TRAFFIC_CATEGORIES,
                    labels: {
                        style: {
                            color: "#abc4e6"
                        }
                    }
                },
                yAxis: {
                    title: false,
                    gridLineColor: '#75a3d7',
                    labels: {
                        style: {
                            color: "#abc4e6"
                        }
                    }
                },
                tooltip: {
                    valueSuffix: ''
                },
                legend: false,
                series: TRAFFIC_DATAS
            });
        },
        dropdownArrowToggler: function () {
            $('.dropdown-toggle').on('click', function (e) {
                e.preventDefault();
                $('.dashboard-sidebar i.pull-right').removeClass('fa-chevron-up').addClass('fa-chevron-down');
                $('.navbar-top .navbar-nav .dropdown > a i').removeClass('fa-chevron-up').addClass('fa-chevron-down');
                if(!$(this).parent().hasClass('open')) {
                    $(this).find('.fa-chevron-down').removeClass('fa-chevron-down').addClass('fa-chevron-up');
                }

            });
        },
        moduleToggle: function () {
            $('.panel-toggle').on('click', function (e) {
                e.preventDefault();
                var $panelBody = $(this).parent().next();
                $panelBody.slideToggle(function () {
                    if($panelBody.css('display') == 'none') {
                        $(this).parent().find('.panel-toggle i').removeClass('fa-caret-up').addClass('fa-caret-down');
                    } else {
                        $(this).parent().find('.panel-toggle i').addClass('fa-caret-up').removeClass('fa-caret-down');
                    }
                });
            });
            $('.dropdown-menu > li > a').on('click', function (e) {
                e.stopPropagation();
            });
        }
    };
    $(document).on('ready', function () {
        window.REVSQUARE.init();
    });
}(jQuery, window, document));
