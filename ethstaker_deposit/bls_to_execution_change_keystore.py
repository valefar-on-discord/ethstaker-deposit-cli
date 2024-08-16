import json
import os
from typing import Any, Dict
from eth_typing import HexAddress
from eth_utils import to_canonical_address
from py_ecc.bls import G2ProofOfPossession as bls

from ethstaker_deposit.exceptions import ValidationError
from ethstaker_deposit.settings import BaseChainSetting
from ethstaker_deposit.utils.ssz import (
    BLSToExecutionChangeKeystore,
    SignedBLSToExecutionChangeKeystore,
    compute_signing_root,
    compute_bls_to_execution_change_keystore_domain,
)


def bls_to_execution_change_keystore_generation(
        chain_settings: BaseChainSetting,
        signing_key: int,
        execution_address: HexAddress,
        validator_index: int) -> SignedBLSToExecutionChangeKeystore:
    if execution_address is None:
        raise ValueError("The execution address should NOT be empty.")
    if chain_settings.GENESIS_VALIDATORS_ROOT is None:
        raise ValidationError("The genesis validators root should NOT be empty "
                              "for this chain to obtain the BLS to execution change.")

    message = BLSToExecutionChangeKeystore(  # type: ignore[no-untyped-call]
        validator_index=validator_index,
        to_execution_address=to_canonical_address(execution_address),
    )
    domain = compute_bls_to_execution_change_keystore_domain(
        fork_version=chain_settings.GENESIS_FORK_VERSION,
        genesis_validators_root=chain_settings.GENESIS_VALIDATORS_ROOT,
    )
    signing_root = compute_signing_root(message, domain)
    signature = bls.Sign(signing_key, signing_root)

    return SignedBLSToExecutionChangeKeystore(  # type: ignore[no-untyped-call]
        message=message,
        signature=signature,
    )


def export_bls_to_execution_change_keystore_json(folder: str,
                                                 signed_execution_change: SignedBLSToExecutionChangeKeystore,
                                                 timestamp: float) -> str:
    signed_bls_to_execution_change_keystore_json: Dict[str, Any] = {}

    address = '0x' + signed_execution_change.message.to_execution_address.hex()  # type: ignore[attr-defined]
    index = signed_execution_change.message.validator_index  # type: ignore[attr-defined]
    signature = '0x' + signed_execution_change.signature.hex()  # type: ignore[attr-defined]

    message = {
        'to_execution_address': address,
        'validator_index': index,
    }
    signed_bls_to_execution_change_keystore_json.update({'message': message})
    signed_bls_to_execution_change_keystore_json.update({'signature': signature})

    filefolder = os.path.join(
        folder,
        'bls_to_execution_change_keystore_signature-%s-%i.json' % (index, timestamp)
    )

    with open(filefolder, 'w') as f:
        json.dump(signed_bls_to_execution_change_keystore_json, f)
    if os.name == 'posix':
        os.chmod(filefolder, int('440', 8))  # Read for owner & group
    return filefolder
