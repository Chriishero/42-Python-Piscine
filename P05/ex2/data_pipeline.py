from abc import ABC, abstractmethod
from typing import Any, Protocol


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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVExport:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        csv_str = ','.join(item for _, item in data)
        print(f"CSV Output:\n{csv_str}")


class JSONExport:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        items = [f'"{f"item_{rank}"}": "{item}"' for rank, item in data]
        json_str = '{' + ', '.join(items) + '}'
        print(f"JSON Output:\n{json_str}")


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            processed = False
            for proc in self._processors:
                if proc.validate(item):
                    proc.ingest(item)
                    processed = True
                    break
            if not processed:
                print("DataStream error - "
                      f"Can't process element in stream: {item}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data\n")
            return
        for proc in self._processors:
            name = type(proc).__name__
            total = len(proc._data) + proc._rank
            remaining = len(proc._data)
            print(f"{name}: total {total} items processed, "
                  f"remaining {remaining} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            outputs = []
            for _ in range(min(nb, len(proc._data))):
                outputs.append(proc.output())
            if outputs:
                plugin.process_output(outputs)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...\n")
    ds = DataStream()
    ds.print_processors_stats()
    print("Registering Processors\n")
    np = NumericProcessor()
    tp = TextProcessor()
    lp = LogProcessor()
    ds.register_processor(np)
    ds.register_processor(tp)
    ds.register_processor(lp)
    batch1 = ['Hello world', [3.14, -1, 2.71],
              [{'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'},
               {'log_level': 'INFO',
                'log_message': 'User wil is connected'}], 42, ['Hi', 'five']]
    print(f"Send first batch of data on stream: {batch1}\n")
    ds.process_stream(batch1)
    print()
    ds.print_processors_stats()
    print()
    print("Send 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExport()
    ds.output_pipeline(3, csv_plugin)
    print()
    ds.print_processors_stats()
    print()
    batch2 = [21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
              [{'log_level': 'ERROR', 'log_message': '500 server crash'},
               {'log_level': 'NOTICE',
                'log_message': 'Certificate expires in 10 days'}],
              [32, 42, 64, 84, 128, 168], 'World hello']
    print(f"Send another batch of data: {batch2}\n")
    ds.process_stream(batch2)
    ds.print_processors_stats()
    print()
    print("Send 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExport()
    ds.output_pipeline(5, json_plugin)
    print()
    ds.print_processors_stats()


if __name__ == "__main__":
    main()
