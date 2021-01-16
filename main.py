# coding=utf-8
import sys

from workflow import Workflow

import generators


GENERATORS = {
    "email": generators.random_email,
    "imei": generators.random_imei,
    "unit": generators.random_unit_number,
    "uuid": generators.random_uuid,
}


def main(workflow):
    param = " ".join(workflow.args).lower()

    if param in GENERATORS:
        items = [param] * 5
    else:
        items = sorted(GENERATORS.keys())

    for name in items:
        value = GENERATORS[name]()

        workflow.add_item(
            title=value,
            subtitle=name,
            arg=value,
            valid=True,
        )


if __name__ == u"__main__":
    wf = Workflow()
    wf.run(main)
    wf.send_feedback()
    sys.exit()
