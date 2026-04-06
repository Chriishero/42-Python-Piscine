
from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid numeric data")
        result = (
            f"Processed {len(data)} numeric values, "
            f"sum={sum(data)}, avg={sum(data)/len(data)}"
        )
        return result

    def validate(self, data: Any) -> bool:
        if not isinstance(data, list) or not data:
            return False
        try:
            return all(isinstance(x, (int, float)) for x in data)
        except Exception:
            return False


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid text data")
        result = (
            f"Processed text: {len(data)} characters, "
            f"{len(data.split())} words"
        )
        return result

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and bool(data)


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid log data")
        if "ERROR" in data:
            message = data.split(': ', 1)[1] if ': ' in data else data
            result = f"[ALERT] ERROR level detected: {message}"
        elif "INFO" in data:
            message = data.split(': ', 1)[1] if ': ' in data else data
            result = f"[INFO] INFO level detected: {message}"
        else:
            result = f"Processed log: {data}"
        return result

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and bool(data)


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    # Numeric
    print("Initializing Numeric Processor...")
    num_data: list[int] = [1, 2, 3, 4, 5]
    print(f"Processing data: {num_data}")
    result = NumericProcessor().process(num_data)
    print("Validation: Numeric data verified")
    print(f"Output: {result}")
    print()
    # Text
    print("Initializing Text Processor...")
    text_data: str = "Hello Nexus World"
    print(f"Processing data: \"{text_data}\"")
    result = TextProcessor().process(text_data)
    print("Validation: Text data verified")
    print(f"Output: {result}")
    print()
    # Log
    print("Initializing Log Processor...")
    log_data: str = "ERROR: Connection timeout"
    print(f"Processing data: \"{log_data}\"")
    result = LogProcessor().process(log_data)
    print("Validation: Log entry verified")
    print(f"Output: {result}")
    print()
    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    processors = [NumericProcessor(), TextProcessor(), LogProcessor()]
    demo_data = [[1, 2, 3], "Hello world!", "INFO: System ready"]
    for i, (proc, d) in enumerate(zip(processors, demo_data), 1):
        result = proc.process(d)
        print(f"Result {i}: {result}")
    print()
    print("Foundation systems online. Nexus ready for advanced streams.")
