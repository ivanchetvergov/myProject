$(function(){
    $('.b-1').on('click',function(){
        let answer = $(this).siblings('.i-1').val()
        let rightAnswer = $(this).siblings('.right-answer').val()
        console.log(answer)
        if(answer !== rightAnswer){
            $(this).siblings('.i-1').removeClass('right-answer__border')
            $(this).siblings('.i-1').addClass('wrong-answer__border')
            $(this).siblings('.right-answer-container').show()
        }else{
            $(this).siblings('.i-1').removeClass('wrong-answer__border')
            $(this).siblings('.i-1').addClass('right-answer__border')
        }
    });
});
