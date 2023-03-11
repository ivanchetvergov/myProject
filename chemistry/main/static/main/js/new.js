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


function first() {
document.getElementById("second_hide").setAttribute("style", "opacity:1; transition: 1s; height: 100%;");
document.getElementById("first").setAttribute("style", "display: none");
document.getElementById("first_yelloy").setAttribute("style", "display: block");
}

function first_yelloy() {
document.getElementById("second_hide").setAttribute("style", "display: none");
document.getElementById("first_yelloy").setAttribute("style", "display: none");
document.getElementById("first").setAttribute("style", "display: block");
}

const btn = document.querySelector(".btn");
const content = document.querySelector(".content");

function btnClick() {
    console.log(content.classList);
    if (content.classList.contains("hidden")) {
        btn.textContent = "Скрыть элемент";
    } else {
        btn.textContent = "Показать элемент";
    }
    content.classList.toggle("hidden");
}