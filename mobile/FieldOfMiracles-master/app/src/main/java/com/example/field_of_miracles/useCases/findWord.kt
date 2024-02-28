package com.example.field_of_miracles.useCases

import kotlin.random.Random

class findWord {

    fun findWordExecute(words: List<String>, index:Int): String{
        val word = words[index]
        return word
    }

    fun findArrayOfLetters(word:String, letter: String): String {
        var i = 0
        var j = 0
        var k = 0
        var str = ""
        var arrayOfLetters = mutableListOf<String>()


            while (i < word.length) {
                arrayOfLetters.add(i, " _ ")
                i++
            }


        while(j<word.length){
            if (word[j].toString() == letter) {
                arrayOfLetters[j] = word[j].toString()
            }
            j++
        }

        while (k < arrayOfLetters.size){
            str += arrayOfLetters[k]
            k++
        }

        return str
    }

}