from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[str] = []
        self._rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise ValueError("No data available")
        item = self._data.pop(0)
        rank = self._rank
        self._rank += 1
        return (rank, item)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, str):
            try:
                float(data)
                return True
            except ValueError:
                return False
        if isinstance(data, list):
            return all(self.validate(x) for x in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if isinstance(data, (int, float)):
            self._data.append(str(data))
        elif isinstance(data, list):
            for x in data:
                if not isinstance(x, (int, float)):
                    raise ValueError("Improper numeric data")
                self._data.append(str(x))
        else:
            raise ValueError("Improper numeric data")


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            try:
                float(data)
                return False
            except ValueError:
                return True
        if isinstance(data, list):
            return all(isinstance(x, str) and self.validate(x) for x in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if isinstance(data, str):
            try:
                float(data)
                raise ValueError("Improper text data")
            except ValueError:
                pass
            self._data.append(data)
        elif isinstance(data, list):
            for s in data:
                if not isinstance(s, str):
                    raise ValueError("Improper text data")
                try:
                    float(s)
                    raise ValueError("Improper text data")
                except ValueError:
                    pass
                self._data.append(s)
        else:
            raise ValueError("Improper text data")


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return 'log_level' in data and 'log_message' in data
        if isinstance(data, list):
            return all(isinstance(d, dict) and 'log_level' in d
                       and 'log_message' in d for d in data)
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        def format_log(d: dict[str, str]) -> str:
            return f"{d['log_level']}: {d['log_message']}"

        if isinstance(data, dict):
            if not ('log_level' in data and 'log_message' in data):
                raise ValueError("Improper log data")
            self._data.append(format_log(data))
        elif isinstance(data, list):
            for d in data:
                if not isinstance(d, dict) or not ('log_level' in d
                                                   and 'log_message' in d):
                    raise ValueError("Improper log data")
                self._data.append(format_log(d))
        else:
            raise ValueError("Improper log data")


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")
    print("Testing Numeric Processor...")
    np = NumericProcessor()
    print(f" Trying to validate input '42': {np.validate('42')}")
    print(f" Trying to validate input 'Hello': {np.validate('Hello')}")
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        np.ingest('foo')  # type: ignore
    except Exception as e:
        print(f" Got exception: {e}")
    np.ingest([1, 2, 3, 4, 5])
    print(" Processing data: [1, 2, 3, 4, 5]")
    print(" Extracting 3 values...")
    for _ in range(3):
        rank, val = np.output()
        print(f" Numeric value {rank}: {val}")
    print("\nTesting Text Processor...")
    tp = TextProcessor()
    print(f" Trying to validate input '42': {tp.validate('42')}")
    tp.ingest(['Hello', 'Nexus', 'World'])
    print(" Processing data: ['Hello', 'Nexus', 'World']")
    print(" Extracting 1 value...")
    rank, val = tp.output()
    print(f" Text value {rank}: {val}")
    print("\nTesting Log Processor...")
    lp = LogProcessor()
    print(f" Trying to validate input 'Hello': {lp.validate('Hello')}")
    lp.ingest([{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
               {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}])
    print(" Processing data: [{'log_level': 'NOTICE',"
          "'log_message': 'Connection to server'}, "
          "{'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]")
    print(" Extracting 2 values...")
    for _ in range(2):
        rank, val = lp.output()
        print(" Log entry", rank, ":", val)


if __name__ == "__main__":
    main()
