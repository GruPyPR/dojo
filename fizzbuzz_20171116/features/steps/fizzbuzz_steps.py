from fizzbuzz import fizzbuzz, FizzBuzzInt


@when('I choose number {number:d}')
def step_impl(context, number):
    context.number = number


@when('call the function')
def step_impl(context):
    context.result = fizzbuzz(context.number)


@then('it should return {number:d}')
def step_impl(context, number):
    assert context.result == number


@then('it should return \'{fizzbuzz_text}\'')
def step_impl(context, fizzbuzz_text):
    assert context.result == fizzbuzz_text


@when('create a FizzBuzzInt object for the number')
def step_impl(context):
    context.obj = FizzBuzzInt(context.number)


@when('call the method to_fizzbuzz')
def step_impl(context):
    context.result = context.obj.to_fizzbuzz()


@then('its repr() should match repr({number:d})')
def step_impl(context, number):
    assert repr(context.result) == repr(number)


@then('its repr() should match repr(\'{fizzbuzz_text}\')')
def step_impl(context, fizzbuzz_text):
    assert repr(context.result) == repr(fizzbuzz_text)


