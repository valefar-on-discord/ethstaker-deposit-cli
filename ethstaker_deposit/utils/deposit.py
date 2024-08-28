import json
import os


def export_deposit_data_json(folder: str, timestamp: float, deposit_data: list[dict[str, bytes]]) -> str:
    file_folder = os.path.join(folder, 'deposit_data-%i.json' % timestamp)
    with open(file_folder, 'w') as f:
        json.dump(deposit_data, f, default=lambda x: x.hex())
    if os.name == 'posix':
        os.chmod(file_folder, int('440', 8))  # Read for owner & group
    return file_folder
