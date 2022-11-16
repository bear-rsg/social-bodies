$(document).ready(function() {

    // Transcription content switches
    $('.transcription-content-switch div').on('click', function(){
        // Make switch active/inactive
        $('.transcription-content-switch div').removeClass('active');
        $(this).addClass('active');
        // Show/hide the text
        var textId = $(this).attr('data-textid');
        $('.transcription-content-section').hide();
        $('#transcription-content-section-' + textId).show();
    });
    // Click the first switch by default
    $('.transcription-content-switch div').first().trigger('click');

    // Show/hide existing transcriptions based on choice from list
    $('#transcription-publicinput-existing-select').on('change', function(){
        // Hide all transcriptions
        $('.transcription-publicinput-existing-instance').hide();
        // Show this transcription
        $('.transcription-publicinput-existing-instance[data-id="' + $(this).val() + '"]').show();
    }).trigger('change');

    // Scroll to an image in the list of images
    function scrollToImage(imageId){

        var topContainer = $('#transcription-images').scrollTop();
        var topThis = $('.transcription-images-image-container[data-imageid="' + imageId + '"]').position().top;
        var topExtra = ($('#transcription-images').hasClass('fullscreen') ? 150 : 400);
        $('#transcription-images').animate({ scrollTop: topContainer + topThis - topExtra }, 400);
    }
    // When focussing on a new public transcription textarea
    $('.transcription-publicinput-new-form-transcribe').on('focus', function(){
        scrollToImage($(this).attr('data-imageid'));
    });
    // When clicking on an existing public transcription
    $('.transcription-publicinput-existing-instance-page').on('click', function(){
        scrollToImage($(this).attr('data-imageid'));
    });

    // Fullscreen:
    // Set button content
    function setFullscreenButtonContent(){
        // Close full screen
        if ($('#detail-fullscreen').hasClass('fullscreen')) $('#detail-fullscreen').html('<i class="fas fa-times"></i>').attr('title', 'Close full screen');
        // Go full screen
        else $('#detail-fullscreen').html('<i class="fas fa-expand-alt"></i>').attr('title', 'Go full screen');
    }
    setFullscreenButtonContent();
    // Toggle full screen
    $('#detail-fullscreen').on('click', function(){
        $('body, #detail-fullscreen, #transcription-images, #transcription-publicinput, #transcription-texts').toggleClass('fullscreen');
        setFullscreenButtonContent();
    });

});