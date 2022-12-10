import sys
from typing import Optional
from dataclasses import dataclass, field


class Instruction:
    pass


@dataclass
class NoopInstruction(Instruction):
    cycles: int = 1

    def execute(self, cpu):
        self.cycles -= 1
        return self.cycles == 0


@dataclass
class AddxInstruction(Instruction):
    x: int
    cycles: int = 2

    def execute(self, cpu):
        self.cycles -= 1
        if self.cycles == 0:
            cpu.x += self.x
            return True


@dataclass
class CRT:
    data: list[list[str]] = field(default_factory=lambda: [" " for _ in range(240)])

    def draw(self, cpu):
        if cpu.clock % 40 in set(range(cpu.x - 1, cpu.x + 2)):
            self.data[cpu.clock] = "█"

    def display(self):
        for y in range(6):
            for x in range(40):
                print(self.data[y * 40 + x], end="")
            print("")


@dataclass
class CPU:
    instructions: list[Instruction] = field(default_factory=list)
    instruction: Optional[Instruction] = None
    clock: int = 0
    x: int = 1

    def tick(self):
        self.clock += 1
        if not self.instruction and self.instructions:
            self.instruction = self.instructions.pop(0)
        if self.instruction.execute(self):
            if self.instructions:
                self.instruction = self.instructions.pop(0)


def main():
    cpu = CPU()
    crt = CRT()

    for instruction in [line.strip().split(" ") for line in sys.stdin.readlines()]:
        match instruction[0]:
            case "noop":
                cpu.instructions.append(NoopInstruction())
            case "addx":
                cpu.instructions.append(AddxInstruction(int(instruction[1])))

    for _ in range(240):
        crt.draw(cpu)
        cpu.tick()
    crt.display()


if __name__ == "__main__":
    main()
