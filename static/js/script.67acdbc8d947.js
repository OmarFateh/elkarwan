$(document).ready(function () {



	// Animate loader off screen
	$(".se-pre-con").fadeOut("slow");

	// Slider Options
	$("#sliderr").slick({
		autoplay: true,
		autoplaySpeed: 7000,
		slidesToShow: 1,
		slidesToScroll: 1,
		pauseOnHover: false,
		dots: true,
		arrows: true,
		pauseOnDotsHover: true,
		cssEase: 'linear',
		fade: true,
		draggable: false,
		prevArrow: '<button class="PrevArrow"> <span class="Thumbnail"></span></button>',
		nextArrow: '<button class="NextArrow"> <span class="Thumbnail"></span></button>',
		// Custom Dots With Thumbnails Tool Tip
		customPaging: function (slider, i) {
			var thumbnail = $(slider.$slides[i]).data('thumbnail');
			return '<a href="javascript:void(0)"><img src="' + thumbnail + '"></a>';
		}
	});

	new WOW().init();
});