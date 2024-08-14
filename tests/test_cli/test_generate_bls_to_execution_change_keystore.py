import os
import time

from click.testing import CliRunner

from ethstaker_deposit.credentials import Credential
from ethstaker_deposit.deposit import cli
from ethstaker_deposit.settings import get_chain_setting
from ethstaker_deposit.utils.constants import DEFAULT_BLS_TO_EXECUTION_CHANGES_KEYSTORE_FOLDER_NAME
from .helpers import (
    clean_btec_keystore_folder,
    clean_key_folder,
    prepare_testing_folder,
    read_json_file,
    verify_file_permission,
)


def test_existing_mnemonic_bls_change_keystore() -> None:
    # Prepare folder
    my_folder_path = prepare_testing_folder(os)
    changes_folder_path = os.path.join(my_folder_path, DEFAULT_BLS_TO_EXECUTION_CHANGES_KEYSTORE_FOLDER_NAME)

    clean_key_folder(my_folder_path)
    if not os.path.exists(my_folder_path):
        os.mkdir(my_folder_path)
    if not os.path.exists(changes_folder_path):
        os.mkdir(changes_folder_path)

    # Shared parameters
    chain = 'mainnet'
    keystore_password = 'solo-stakers'

    # Prepare credential
    credential = Credential(
        mnemonic='aban aban aban aban aban aban aban aban aban aban aban abou',
        mnemonic_password='',
        index=0,
        amount=0,
        chain_setting=get_chain_setting(chain),
        hex_withdrawal_address=None
    )

    # Save keystore file
    keystore_filepath = credential.save_signing_keystore(keystore_password, changes_folder_path, time.time())

    runner = CliRunner()
    arguments = [
        '--language', 'english',
        '--non_interactive',
        'generate-bls-to-execution-change-keystore',
        '--output_folder', my_folder_path,
        '--chain', chain,
        '--keystore', keystore_filepath,
        '--keystore_password', keystore_password,
        '--validator_index', '1',
        '--withdrawal_address', '0xcd60A5f152724480c3a95E4Ff4dacEEf4074854d',
    ]
    result = runner.invoke(cli, arguments)

    assert result.exit_code == 0

    # Check files
    _, _, files = next(os.walk(changes_folder_path))

    change_files = [f for f in files if 'bls_to_execution_change_keystore_' in f]

    assert len(set(change_files)) == 1

    json_data = read_json_file(changes_folder_path, change_files[0])

    # Verify file content
    assert json_data['message']['to_execution_address'] == '0xcd60a5f152724480c3a95e4ff4daceef4074854d'
    assert json_data['message']['validator_index'] == 1
    assert json_data['signature']

    # Verify file permissions
    verify_file_permission(os, folder_path=changes_folder_path, files=change_files)

    # Clean up
    clean_btec_keystore_folder(my_folder_path)
