$(document).ready(function() {

    // Image magnifying glass
    $('.transcription-images-image-container').on('mousemove', function(e){
        console.log(1)
        var this_main_img_id = $(this).find('.main-img').attr('id'),
        this_zoomed_img_id = $(this).find('.zoomed-img').attr('id'),
            original = document.getElementById(this_main_img_id),
            magnified = document.getElementById(this_zoomed_img_id),
            style = magnified.style,
            x = e.pageX - this.offsetLeft,
            y = e.pageY - this.offsetTop,
            imgWidth = original.width,
            imgHeight = original.height,
            xperc = (x / imgWidth) * 100,
            yperc = (y / imgHeight) * 100;
        // Add some margin for right edge
        if (x > 0.01 * imgWidth) xperc += 0.15 * xperc;
        // Add some margin for bottom edge
        if (y >= 0.01 * imgHeight) yperc += 0.15 * yperc;
        // Set the background of the magnified image horizontal
        style.backgroundPositionX = xperc - 9 + '%';
        // Set the background of the magnified image vertical
        style.backgroundPositionY = yperc - 9 + '%';
        // Move the magnifying glass with the mouse movement.
        var width_height_half = 125; // whatever value here (e.g. 125) must be double in CSS width & height (e.g. 250px)
        style.left = x - width_height_half + 'px';
        style.top = y - width_height_half + 'px';
    });

    // Transcription text switches
    $('#transcription-texts-switch div').on('click', function(){
        // Make switch active/inactive
        $('#transcription-texts-switch div').removeClass('active');
        $(this).addClass('active');
        // Show/hide the text
        var textId = $(this).attr('data-textid');
        $('.transcription-texts-text').hide();
        $('#transcription-texts-text-' + textId).show();
    });
    // Click the first switch by default
    $('#transcription-texts-switch div').first().trigger('click');

});