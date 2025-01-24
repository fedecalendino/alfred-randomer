import sys
from typing import List

from pyflow import Workflow

import generators


GENERATORS = {
    "email": generators.random_email,
    "imei": generators.random_imei,
    "unit": generators.random_unit_number,
    "uuid": generators.random_uuid,
}


def parse_args(args: List[str]) -> tuple:
    if len(args) >= 2:
        return args[0].lower(), int(args[1])

    if len(args) == 1:
        try:
            return None, int(args[0])
        except ValueError:
            return args[0].lower(), 1

    return None, 1


def main(workflow):
    generator, amount = parse_args(workflow.args)

    if generator in GENERATORS:
        items = [generator] * 5
    else:
        items = sorted(GENERATORS.keys())

    for name in items:
        values = [GENERATORS[name]() for _ in range(amount)]

        workflow.new_item(
            title=values[0],
            subtitle=f"{name} x {amount}",
            arg="\n".join(values),
            valid=True,
        )


if __name__ == "__main__":
    wf = Workflow()
    wf.run(main)
    wf.send_feedback()
    sys.exit()
