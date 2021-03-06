# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.broccoli.base import BROCCOLICommand

def test_BROCCOLICommand_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    device=dict(argstr='-device %d',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    output=dict(argstr='-output %s',
    ),
    output_type=dict(),
    platform=dict(argstr='-platform %d',
    ),
    quiet=dict(argstr='-quiet',
    ),
    terminal_output=dict(nohash=True,
    ),
    verbose=dict(argstr='-verbose',
    ),
    )
    inputs = BROCCOLICommand.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

