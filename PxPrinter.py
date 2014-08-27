import gdb

def printInner(v, c):
    if c == None:
        for k in v.type.keys():
            try:
                v_ = v[k]
            except gdb.error:
                continue
            gdb.write('%s: %s \n' % (k, v_))
    else:
        gdb.write('%s: %s \n' % (c, v[c]))

class PxPrinter(gdb.Command):
    def __init__(self):
        super(PxPrinter, self).__init__(
                'ppx', gdb.COMMAND_DATA, gdb.COMPLETE_SYMBOL, False)
    def invoke(self, arg, from_tty):
        space_location = arg.find(' ')
        if space_location == -1:
            (expr, component) = (arg, None)
        else:
            (expr, component) = (arg[:space_location], arg[space_location+1:])
        try:
            v = gdb.parse_and_eval(expr)
        except gdb.error, e:
            raise gdb.GdbError(e.message)
        printInner(v, component)

PxPrinter()
