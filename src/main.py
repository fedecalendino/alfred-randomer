import sys

from pyflow import Workflow

import generators

GENERATORS = {
    "email": generators.random_email,
    "imei": generators.random_imei,
    "unit": generators.random_unit_number,
    "uuid": generators.random_uuid,
    "phone": generators.random_phone,
    "phoneus": generators.random_phone_us,
    "phoneuk": generators.random_phone_uk,
    "phonerr": generators.random_phone_rr,
    "phonecn": generators.random_phone_cn,
}


def main(workflow):
    param = " ".join(workflow.args).lower()

    if param in GENERATORS:
        items = [param] * 5
    else:
        items = sorted(GENERATORS.keys())

    for name in items:
        value = GENERATORS[name]()

        workflow.new_item(
            title=value,
            subtitle=name,
            arg=value,
            valid=True,
        )


if __name__ == "__main__":
    wf = Workflow()
    wf.run(main)
    wf.send_feedback()
    sys.exit()
