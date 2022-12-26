def example():
    n = 1.0
    for _ in range(10):
        n += 1
    return n
import dis
dis.disassemble(example.__code__)