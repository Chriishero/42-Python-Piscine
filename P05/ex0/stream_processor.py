
from typing import Any, List
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        print("Initializing Data Processor...")
        print(f"Processing data: {data}")
        if not self.validate(data):
            print("Validation: Data are not conform")
        else:
            print("Validation: Data verified")
        output = self.format_output(data)
        print(output)
        return (output)

    def validate(self, data: Any) -> bool:
        if data is None or DataProcessor.ft_len(data) == 0:
            return (False)
        else:
            return (True)

    @abstractmethod
    def format_output(self, result: str) -> str:
        try:
            return f"Processed data: {DataProcessor.ft_len(result)}"
        except Exception as e:
            return f"[ALERT] ERROR {e}"

    @staticmethod
    def ft_len(data: Any) -> int:
        i = 0
        while True:
            try:
                data[i]
                i += 1
            except IndexError:
                return i


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def process(self, data: Any) -> str:
        print("Initializing Numeric Processor...")
        print(f"Processing data: {data}")
        if not self.validate(data):
            print("Validation: Numeric data are not conform")
        else:
            print("Validation: Numeric data verified")
        output = self.format_output(data)
        return (output)

    def format_output(self, result: str) -> str:
        try:
            return (f"Processed {DataProcessor.ft_len(result)} numeric values,"
                    f" sum={NumericProcessor.ft_sum(result)}, "
                    f"avg={NumericProcessor.ft_avg(result)}")
        except Exception as e:
            return f"[ALERT] ERROR {e}"

    @staticmethod
    def ft_sum(data: List) -> int:
        sum = 0
        for d in data:
            sum += d
        return (sum)

    @staticmethod
    def ft_avg(data: List) -> float:
        return (NumericProcessor.ft_sum(data) / DataProcessor.ft_len(data))


class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def process(self, data: str) -> str:
        print("Initializing Text Processor...")
        print(f'Processing data: "{data}"')
        if not self.validate(data):
            print("Validation: Text data are not conform")
        else:
            print("Validation: Text data verified")
        output = self.format_output(data)
        return (output)

    def format_output(self, data: str) -> str:
        try:
            return (f"Processed text: "
                    f"{DataProcessor.ft_len(data)} characters, "
                    f"{TextProcessor.ft_count_word(data)} words")
        except Exception as e:
            return f"[ALERT] ERROR {e}"

    @staticmethod
    def ft_count_word(s: str) -> int:
        word_count = 0
        word = False
        for c in s:
            if c != ' ' and word is False:
                word_count += 1
                word = True
            elif c == ' ':
                word = False
        return (word_count)


class LogProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def process(self, data: List) -> str:
        print("Initializing Log Processor...")
        print(f'Processing data: "{data}"')
        if not self.validate(data):
            print("Validation: Log entry are not conform")
        else:
            print("Validation: Log entry verified")
        output = self.format_output(data)
        return (output)

    def validate(self, data: str) -> bool:
        if data is None or DataProcessor.ft_len(data) == 0:
            return (False)
        else:
            return (True)

    def format_output(self, data: str) -> str:
        try:
            if "ERROR" in data:
                return (f"[ALERT] {data}")
            elif "INFO" in data:
                return (f"[INFO] {data}")
            else:
                return (f"Processed log: {data}")
        except Exception as e:
            return f"[ALERT] ERROR {e}"


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    print(f"Output: {NumericProcessor().process([1, 5, 3, 5, 6])}\n")
    print(f"Output: {TextProcessor().process('Hello world!')}\n")
    print(f"Output: {LogProcessor().process('ERROR: Connection timeout')}\n")
    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data type through same interface...")
    print("Result 1:", NumericProcessor().format_output([1, 5, 3, -4]))
    print("Result 2:", TextProcessor().format_output('waaa ouiiiiiiiiiii n'))
    print("Result 3:", LogProcessor().format_output("INFO: System ready"))
    print("\nFoundation systems online. Nexus ready for advanced streams.")
