import click
import pyperclip
from typing import (
    Any,
    Callable,
)

from ethstaker_deposit.exceptions import ValidationError
from ethstaker_deposit.key_handling.key_derivation.mnemonic import (
    reconstruct_mnemonic,
)
from ethstaker_deposit.utils.constants import (
    MNEMONIC_LANG_OPTIONS,
    WORD_LISTS_PATH,
)
from ethstaker_deposit.utils.click import (
    captive_prompt_callback,
    jit_option,
)
from ethstaker_deposit.utils.intl import fuzzy_reverse_dict_lookup, load_text
from ethstaker_deposit.utils.validation import validate_int_range
from .generate_keys import (
    generate_keys,
    generate_keys_arguments_decorator,
)


def load_mnemonic_arguments_decorator(function: Callable[..., Any]) -> Callable[..., Any]:
    '''
    This is a decorator that, when applied to a parent-command, implements the
    to obtain the necessary arguments for the generate_keys() subcommand.
    '''
    decorators = [
        jit_option(
            callback=validate_mnemonic,
            help=lambda: load_text(['arg_mnemonic', 'help'], func='existing_mnemonic'),
            param_decls='--mnemonic',
            prompt=lambda: load_text(['arg_mnemonic', 'prompt'], func='existing_mnemonic'),
            type=str,
        ),
        jit_option(
            callback=captive_prompt_callback(
                lambda x: x,
                lambda: load_text(['arg_mnemonic_password', 'prompt'], func='existing_mnemonic'),
                lambda: load_text(['arg_mnemonic_password', 'confirm'], func='existing_mnemonic'),
                lambda: load_text(['arg_mnemonic_password', 'mismatch'], func='existing_mnemonic'),
                hide_input=True,
            ),
            default='',
            help=lambda: load_text(['arg_mnemonic_password', 'help'], func='existing_mnemonic'),
            hidden=True,
            param_decls='--mnemonic_password',
            prompt=False,
        ),
        jit_option(
            callback=lambda _, __, language: fuzzy_reverse_dict_lookup(language, MNEMONIC_LANG_OPTIONS),
            default=None,
            help=lambda: "Replace me",
            param_decls='--mnemonic_language',
            prompt=None,
        ),
    ]
    for decorator in reversed(decorators):
        function = decorator(function)
    return function


def validate_mnemonic(ctx: click.Context, param: Any, mnemonic: str) -> str:
    mnemonic_language = ctx.params.get('mnemonic_language')
    mnemonic = reconstruct_mnemonic(mnemonic, WORD_LISTS_PATH, mnemonic_language)
    if mnemonic is not None:
        return mnemonic
    else:
        raise ValidationError(load_text(['err_invalid_mnemonic']))


@click.command(
    help=load_text(['arg_existing_mnemonic', 'help'], func='existing_mnemonic'),
)
@load_mnemonic_arguments_decorator
@jit_option(
    callback=captive_prompt_callback(
        lambda num: validate_int_range(num, 0, 2**32),
        lambda: load_text(['arg_validator_start_index', 'prompt'], func='existing_mnemonic'),
        lambda: load_text(['arg_validator_start_index', 'confirm'], func='existing_mnemonic'),
        prompt_if_none=True,
    ),
    default=0,
    help=lambda: load_text(['arg_validator_start_index', 'help'], func='existing_mnemonic'),
    param_decls="--validator_start_index",
    prompt=False,  # the callback handles the prompt
)
@generate_keys_arguments_decorator
@click.pass_context
def existing_mnemonic(ctx: click.Context, mnemonic: str, mnemonic_password: str, **kwargs: Any) -> None:
    ctx.obj = {} if ctx.obj is None else ctx.obj  # Create a new ctx.obj if it doesn't exist
    ctx.obj.update({'mnemonic': mnemonic, 'mnemonic_password': mnemonic_password})
    # Clear clipboard
    try:  # Failing this on headless Linux is expected
        pyperclip.copy(' ')
    except Exception:
        pass
    ctx.forward(generate_keys)
