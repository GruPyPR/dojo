from jokenpo import jokenpo, JogadaInvalidaError


@when('one player chooses None')
def step_impl(context):
    context.hand_player1 = None


@when('one player chooses {hand:d}')
def step_impl(context, hand):
    context.hand_player1 = hand


@when('one player chooses {hand}')
def step_impl(context, hand):
    context.hand_player1 = hand


@when('the other player chooses {hand}')
def step_impl(context, hand):
    context.hand_player2 = hand


@then('the winner hand should be {winner}')
def step_impl(context, winner):
    assert context.exception is None
    assert context.result == winner


@when('players show their hands')
def step_impl(context):
    context.exception = None
    try:
        context.result = jokenpo(context.hand_player1, context.hand_player2)
    except Exception as e:
        context.exception = e


@then('we should get and error')
def step_impl(context):
    assert isinstance(context.exception, JogadaInvalidaError)



