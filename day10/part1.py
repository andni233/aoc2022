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
class CPU:
    instructions: list[Instruction] = field(default_factory=list)
    instruction: Optional[Instruction] = None
    clock: int = 0
    x: int = 1

    def tick(self):
        self.clock += 1
        if not self.instruction or self.instruction.execute(self):
            if self.instructions:
                self.instruction = self.instructions.pop(0)

    def signal_strength_after(self, ticks):
        for _ in range(ticks):
            self.tick()
        return self.clock * self.x


def main():
    cpu = CPU()

    for instruction in [line.strip().split(" ") for line in sys.stdin.readlines()]:
        match instruction[0]:
            case "noop":
                cpu.instructions.append(NoopInstruction())
            case "addx":
                cpu.instructions.append(AddxInstruction(int(instruction[1])))

    print(sum([cpu.signal_strength_after(ticks) for ticks in [20, 40, 40, 40, 40, 40]]))


if __name__ == "__main__":
    main()
