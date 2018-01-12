Feature: Play Jokenpo game

    Scenario Outline: See who is the winner from two hands of play
        When one player chooses <player1_hand>
         And the other player chooses <player2_hand>
         And players show their hands
        Then the winner hand should be <winner>

        Examples: players hands and winner
            | player1_hand | player2_hand |  winner    |
            |    pedra     |    pedra     |  EMPATE    |
            |    pedra     |    tesoura   |  PEDRA     |
            |    pedra     |    papel     |  PAPEL     |
            |    tesoura   |    papel     |  TESOURA   |
            |    tesoura   |    pedra     |  PEDRA     |
            |    tesoura   |    tesoura   |  EMPATE    |
            |    papel     |    papel     |  EMPATE    |
            |    papel     |    pedra     |  PAPEL     |
            |    papel     |    tesoura   |  TESOURA   |
            |    Papel     |    pedra     |  PAPEL     |
            |    papel     |    Pedra     |  PAPEL     |


    Scenario Outline: Try to play with invalid hands
        When one player chooses <player1_hand>
         And the other player chooses <player2_hand>
         And players show their hands
        Then we should get and error

        Examples: invalid players hands
            | player1_hand | player2_hand |
            |    preda     |    preda     |
            |    tezoura   |    preda     |
            |    preda     |    tesoura   |
            |    1         |    pedra     |
            |    pedra     |    1         |
            |    None      |    pedra     |
            |    pedra     |    None      |

