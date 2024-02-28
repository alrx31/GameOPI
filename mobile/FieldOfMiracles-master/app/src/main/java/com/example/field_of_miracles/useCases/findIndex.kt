package com.example.field_of_miracles.useCases

import kotlin.random.Random

class findIndex {

    fun findWordIndex(words: List<String>):Int{
        val index = Random.nextInt(0,words.size-1)
        return index
    }

    fun findScoreIndex(scores: List<Int>):Int{
        val index = Random.nextInt(0,scores.size-1)
        return index
    }

}