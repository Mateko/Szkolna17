$(function() {
    $('#lifePreserver').submit(function(e) {
        e.preventDefault()
        lifePreserver = $(this).find("input[type=submit]:focus").attr('id')
        lifePreserverValue(lifePreserver)
    });

    function lifePreserverValue(lifePreserver) {
        $.ajax({
            url: "life_preserver/",
            type: "POST",
            data: {
                csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
                life_preserver: lifePreserver
            },
            dataType: "json"
        });
        
        const answerOne = $('#answer1').attr('value')
        const answerTwo = $('#answer2').attr('value')
        const answerThree = $('#answer3').attr('value')
        const answerFour = $('#answer4').attr('value')
        id = '#' + lifePreserver

        if (id == '#call_major') {
            document.getElementById('major_pierdol_sie').play()
            $(id).css("pointer-events", "none")
            $(id).css("background", "#DC143C")

        } else if (id == '#fifty_fifty') {
            $(id).css("pointer-events", "none")
            $(id).css("background", "#DC143C")   
            const listOfAnswer = [answerOne, answerTwo, answerThree, answerFour]
            indexOfCorrectAnswer = listOfAnswer.indexOf(correctAnswer)
           
            if (indexOfCorrectAnswer != -1) {
                listOfAnswer.splice(indexOfCorrectAnswer, 1)
                listOfAnswer.splice(1, 1);
            }

            for (x in listOfAnswer) {
                if (listOfAnswer[x] === answerOne) {
                    $('#answer1').css("pointer-events", "none")
                    $('#answer1').css("visibility", "hidden")
                } else if (listOfAnswer[x] === answerTwo) {
                    $('#answer2').css("pointer-events", "none")
                    $('#answer2').css("visibility", "hidden")
                } else if (listOfAnswer[x] === answerThree) {
                    $('#answer3').css("pointer-events", "none")
                    $('#answer3').css("visibility", "hidden")
                } else if (listOfAnswer[x] === answerFour) {
                    $('#answer4').css("pointer-events", "none")
                    $('#answer4').css("visibility", "hidden")
                }
            }

        } else {
            $(id).css("pointer-events", "none")
            $(id).css("background", "#DC143C")

            listOfAnswer = [answerOne, answerTwo, answerThree, answerFour]
            $("#image").hide()
            $("#plot").show()
            const valueOne = Math.floor((Math.random() * 26) + 9)
            const valueTwo = Math.floor((Math.random() * 26) + 9)
            const valueThree = Math.floor((Math.random() * 26) + 9)
            const valueFour = 100 - (valueOne + valueTwo + valueThree)

            const chart = [{
                x: [answerOne, answerTwo, answerThree, answerFour],
                y: [valueOne, valueTwo, valueThree, valueFour],
                type: 'bar'
            }];

            Plotly.newPlot('plot', chart)
        }
    };
});