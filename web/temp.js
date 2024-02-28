
    import {words, baraban} from "./data.js"
    let STBUT = document.querySelector('.start_button')
    let STPage = document.querySelector('.start_page')
    let GamePage = document.querySelector('.game_page')
    let input_letter_doc = document.querySelector('#input_letter')


    STBUT.addEventListener('click', () => {
        STPage.classList.toggle('close');
        GamePage.classList.toggle('active')
        setTimeout(() => {
        }, 1000)
        game(words, baraban)
    })


    function game(words, baraban) {
        let Pword = document.querySelector('#word')
        let DEFword = document.querySelector('#definition')
        let TempText = document.querySelector('#temp_text')
        let input_letter_text = document.querySelector('#input_letter_text')
        let baraban_text = document.querySelector('#baraban_text')

        let players = {
            'pl1': {
                'count': 0,
                'name': "Player 1",
            },
            'pl2': {
                'count': 0,
                'name': "Player 2",
            },
            'pl3': {
                'count': 0,
                'name': "Player 3",
            },
        }

        let my_word = words[Math.ceil(Math.random() * (words.length - 1))]
        let word = my_word.split('#')[0]
        let description = my_word.split('#')[1]
        let result = []
        let input_letter = ''
        let entered_words = ['asdfadf', 'adfaf']


        for (let i = 0; i < word.length; i++) {
            result[i] = '_'
        }

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                input_letter = input_letter_doc.value.toUpperCase()
                input_letter_doc.value = ''

            }
        })


        DEFword.innerHTML = description

        let player_flag = 1

        while (result.join('') !== word) {

            TempText.innerHTML = `ход игрока номер ${player_flag % 3 === 0 ? 3 : player_flag % 3}`
            Pword.innerHTML = result.join(' ')
            input_letter_text.innerHTML = ''
            let baraban_value = baraban[Math.ceil(Math.random() * (baraban.length - 1))]

            if (baraban_value === -1) {
                TempText.innerHTML = 'Вы пропускаете ход'
                setTimeout(() => {
                }, 1000)
                player_flag += 1
                continue
            }
            if (baraban_value === 0) {
                TempText.innerHTML = "Сектор + на барабане"
                input_letter_text.innerHTML = "введите номер буквы"

                let interval1 = setInterval(() => {
                    TempText.innerHTML = ''
                    if (input_letter !== '') {
                        if (!isNaN(input_letter)) {
                            if (+input_letter <= 0 || +input_letter > result.length) {
                                TempText.innerHTML = "неверный номер буквы, введите другую"
                                input_letter = ''
                            } else {
                                input_letter = word[+input_letter - 1]
                                clearInterval(interval1)
                            }
                        }
                    }
                }, 1000)

                for (let i = 0; i < result.length; i++) {
                    if (input_letter === word[i]) {
                        result[i] = word[i]
                    }
                }
                player_flag += 1
                input_letter = ''
                Pword.innerHTML = result.join(' ')
                continue
            }

            baraban_text.innerHTML = `Очков на барабане: ${baraban_value}`
            input_letter_text.innerHTML = "Введите букву"

            let interval2 = setInterval(() => {
                TempText.innerHTML = ''
                if (input_letter !== '') {
                    if (entered_words.includes(input_letter)) {
                        TempText.innerHTML = 'такая буква уже была , введите другую'
                        input_letter = ''
                    } else {
                        entered_words.push(input_letter)
                        clearInterval(interval2)
                    }
                }
            }, 1000)

            let game_flag = 0
            for (let i = 0; i < result.length; i++) {
                if (input_letter === word[i]) {
                    result[i] = word[i]
                    game_flag += 1
                }
            }
            if (baraban_value >= 100) {
                players[player_flag % 3 !== 0 ? ('pl' + String(player_flag % 3)) : 'pl3']['count'] += game_flag * baraban_value
            }
            Pword.innerHTML = result.join(' ')
            game_flag === 0 ? player_flag += 1 : player_flag += 0
            input_letter = ''
        }


        console.log("YOU ARE The Winner")
    }


    // ==============Logic=====================

// Game(
// Запуск игры
// Отрисовка описания , ячеек слова, 

// CheckBaraban (players_flag)
// )

// Turn(
// Проверка введённого значения и выдача ошибки в ином случае (alert)
// Когда введено значение с клавиатуры выполнить расчет

// Switch()
// )

// CheckBaraban(
// Проверка значения барабана 
// Вывод чей сейчас ход

// При условии addeventlistener Turn(значение нужно вводить букву или число(сектор +))
// При условии Switch()

// Removeeventlistener turn()
// )
// Switch(
// Смена хода игрока
// )

// ==============Code=====================

function Switch(players_flag){
    Players_flag += 1
    CheckBaraban (players_flag)
    }
    
    function turn(isSectorPlus, players_flag){
    Input_letter = запрос введённого значения
    
    If (isSectorPlus){
    Проверка введённого значения на номер 
    
    
    Return если ошибка
    }Else{
    Проверка введённого значения на букву
    
    Return если ошибка
    }
    Document.Removeeventlistener('keydown')
    Switch(players_flag)
    }
    
    
    Function CheckBaraban(players_flag){
    Let isSectorPlus = false
    If(baraban__value === 0){
    IsSectorPlus= true
    }
    
    If (baraban__value==-1){
    //Вы пропускает ход
    Switch(players___flag)
    Return
    }
    
    Document.addeventlistener('keydown',(e)=>{
    If(e.key == 'Enter'){
    Turn(isSectorPlus, players_flag)
    }
    
    })
    Switch(players_flag)
    }
    
    
    
    Game(words, baraban){
    //Создание локальных переменных
    
    //Вывод условия
    
    Let players_flag = 1
    CheckBaraban(players_flag)
    Return
    }
    
    
    
    Vinner(player_flag){
    
    }