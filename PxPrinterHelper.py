import gdb

def printInnerTest(v):
    # test print method helps develop this script
    if 'px' in v.type.keys():
        v = v['px']
    gdb.write('type:%s; type.target:%s\n' % (v.type, v.type.target()))
    gdb.write('%s\n' % ( v.cast ( v.type ).dereference() ) )

class PxPrinterHelper(gdb.Command):
    """
    PxPrinterHelper: a helper tool for print out developer aware information about gdb
    and the target value
    """
    def __init__(self):
        super(PxPrinterHelper, self).__init__(
                'ppxhelper', gdb.COMMAND_DATA, gdb.COMPLETE_SYMBOL, False)
    def invoke(self, arg, from_tty):
        try:
            v = gdb.parse_and_eval(arg)
        except gdb.error, e:
            raise gdb.GdbError(e.message)
        printInnerTest(v)

PxPrinterHelper()
