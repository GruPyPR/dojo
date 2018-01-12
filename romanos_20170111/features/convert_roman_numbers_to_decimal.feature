Feature: Convert roman number to decimal

    Scenario Outline: Enter a roman number and see it in decimal
        When I enter the roman number <roman_number>
        Then it should show me the decimal number <decimal_number>

        Examples: number in roman and decimal
            | roman_number | decimal_number |
            |    I         |           1    | 
            |    V         |           5    | 
            |    X         |          10    | 
            |    L         |          50    | 
            |    C         |         100    | 
            |    D         |         500    | 
            |    M         |        1000    | 
            |    II        |           2    | 
            |    III       |           3    | 
            |    XX        |          20    | 
            |    VI        |           6    | 
            |    VII       |           7    | 
            |    VIII      |           8    | 
            |    IV        |           4    | 
            |    IX        |           9    | 
            |    IL        |          49    | 
            |    MDXC      |        1590    | 
            |    MCMLXXXIV |        1984    | 
            |    LII       |          52    | 


