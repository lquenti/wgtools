#!/bin/bash

SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

source "$SCRIPT_DIR/venv/bin/activate"

python3 "$SCRIPT_DIR/generate_trash_message/generate_trash_message.py" | python3 "$SCRIPT_DIR/send_to_wg/send_to_wg.py"
