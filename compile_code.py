# import dis
import byteplay
import sys
# from pprint import pprint


def parse_co_code_to_str(code):
    c = byteplay.Code.from_code(code)
# pprint(c.code)
# print(list(c.code))

    def format_label(l):
        return "LABEL, {0}".format(id(l))

    for op in c.code:
        # Byteplay print the actual argument instead of the index. But we are
        # Converting them back to the index in case we want to use other bytecode
        # disassembler in the future.
        # Here is a list of meanings for the arguments
        #   The argument of opcodes in hasconst is the actual constant.
        #   The argument of opcodes in hasname is the name, as a string.
        #   The argument of opcodes in hasjump is a Label instance, which should point to a specific location in the code list.
        #   The argument of opcodes in haslocal is the local variable name, as a string.
        #   The argument of opcodes in hascompare is the string representing the comparison operator.
        #   The argument of opcodes in hasfree is the name of the cell or free variable, as a string.
        if op[0] in byteplay.hasconst:
            print("{0}, {1}".format(op[0], code.co_consts.index(op[1])))
            #print("{0}, {1}".format(op[0], None))
        elif op[0] in byteplay.hasname:
            print("{0}, {1}".format(op[0], code.co_names.index(op[1])))
        elif op[0] in byteplay.hasjump:
            print("{0}, {1}".format(op[0], id(op[1])))
        elif op[0] in byteplay.hascompare:
            print("{0}, {1}".format(op[0], byteplay.cmp_op.index(op[1])))
        elif type(op[0]) == byteplay.Label:
            assert(op[1] == None)
            print(format_label(op[0])) # Is the second argument always None?
            # print("{0}, {1}".format(format_label(op[0]), op[1]))
        else:
            print("{0}, {1}".format(op[0], op[1]))

def main():

    filename = sys.argv[1]
    with open(filename, 'rU') as f:
        code = f.read()

    code = compile(code, filename, "exec")
    print("CONSTS: {0}".format(code.co_consts))
    print("NAMES: {0}".format(code.co_names))
# print(code.co_varnames)
# print(list(bytearray(code.co_code)))
# for elem in list(bytearray(code.co_code)):
#     print(dis.opname[elem])
# dis_output = dis.dis(code)

    parse_co_code_to_str(code)

if __name__ == "__main__":
    main()
