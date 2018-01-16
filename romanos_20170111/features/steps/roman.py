from romanos import romanos


@when('I enter the roman number {roman_number}')
def step_impl(context, roman_number):
    context.decimal_result = romanos(roman_number)


@then('it should show me the decimal number {decimal_number:d}')
def step_impl(context, decimal_number):
    assert context.decimal_result == decimal_number


