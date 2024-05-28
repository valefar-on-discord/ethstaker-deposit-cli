import json
import os
import time
from typing import Any, Dict
from py_ecc.bls import G2ProofOfPossession as bls

from staking_deposit.settings import BaseChainSetting
from staking_deposit.utils.ssz import (
    SignedVoluntaryExit,
    VoluntaryExit,
    compute_signing_root,
    compute_voluntary_exit_domain,
)


def exit_transaction_generation(
        chain_settings: BaseChainSetting,
        signing_key: int,
        validator_index: int,
        epoch: int) -> SignedVoluntaryExit:
    message = VoluntaryExit(  # type: ignore[no-untyped-call]
        epoch=epoch,
        validator_index=validator_index
    )

    domain = compute_voluntary_exit_domain(
        fork_version=chain_settings.EXIT_FORK_VERSION,
        genesis_validators_root=chain_settings.GENESIS_VALIDATORS_ROOT
    )

    signing_root = compute_signing_root(message, domain)
    signature = bls.Sign(signing_key, signing_root)

    signed_exit = SignedVoluntaryExit(  # type: ignore[no-untyped-call]
        message=message,
        signature=signature,
    )

    return signed_exit


def export_exit_transaction_json(folder: str, signed_exit: SignedVoluntaryExit) -> str:
    signed_exit_json: Dict[str, Any] = {}
    message = {
        'epoch': str(signed_exit.message.epoch),  # type: ignore[attr-defined]
        'validator_index': str(signed_exit.message.validator_index),  # type: ignore[attr-defined]
    }
    signed_exit_json.update({'message': message})
    signed_exit_json.update({'signature': '0x' + signed_exit.signature.hex()})  # type: ignore[attr-defined]

    filefolder = os.path.join(
        folder,
        'signed_exit_transaction-%s-%i.json' % (
            signed_exit.message.validator_index, time.time()  # type: ignore[attr-defined]
        )
    )

    with open(filefolder, 'w') as f:
        json.dump(signed_exit_json, f)
    if os.name == 'posix':
        os.chmod(filefolder, int('440', 8))  # Read for owner & group
    return filefolder
