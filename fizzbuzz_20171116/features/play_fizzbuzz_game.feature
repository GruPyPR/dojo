Feature: Play FizzBuzz game
    Fizz buzz is a group word game for children to teach them about division [1].
    Players take turns to count incrementally, replacing any number divisible
    by three with the word "fizz", and any number divisible by five with the
    word "buzz". Numbers divisible by both become "fizzbuzz".
    [1] https://en.wikipedia.org/wiki/Fizz_buzz


    Scenario Outline: Function fizzbuzz should return correclty for each number input
        When I choose number <number>
         And call the function
        Then it should return <fizzbuzz>

    Examples:
        | number | fizzbuzz   |
        |   1    |      1     |
        |   2    |      2     |
        |   3    |   'fizz'   |
        |   4    |      4     |
        |   5    |   'buzz'   |
        |   6    |   'fizz'   |
        |   7    |      7     |
        |   9    |   'fizz'   |
        |  10    |   'buzz'   |
        |  15    | 'fizzbuzz' |


    Scenario Outline: Method to_fizzbuzz from object Fizzbuzz should return correclty
        When I choose number <number>
         And create a FizzBuzzInt object for the number
         And call the method to_fizzbuzz 
        Then it should return <fizzbuzz>
	 And its repr() should match repr(<fizzbuzz>)

    Examples:
        | number | fizzbuzz   |
        |   1    |      1     |
        |   2    |      2     |
        |   3    |   'fizz'   |
        |   4    |      4     |
        |   5    |   'buzz'   |
        |   6    |   'fizz'   |
        |   7    |      7     |
        |   9    |   'fizz'   |
        |  10    |   'buzz'   |
        |  15    | 'fizzbuzz' |
