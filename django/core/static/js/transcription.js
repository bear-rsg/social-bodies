$(document).ready(function() {

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