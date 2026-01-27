
from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


def ft_len(data: Any) -> int:
    i = 0
    for _ in data:
        i += 1
    return i


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.processed_batches = 0
        self.processed_data = []

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return (data_batch)
        else:
            return ([datum for datum in data_batch if criteria in datum])

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return ({
            "stream_id": self.stream_id,
            "processed_batches": self.processed_batches,
            "processed_data": self.processed_data
                 })


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed_batches += 1
        try:
            print(f"Processing sensor batch: {data_batch}")
            self.processed_data = [*self.processed_data,
                                   f"{ft_len(data_batch)} readings processed"]
            print(f"Sensor analysis: {self.processed_data[-1]}")
        except Exception as e:
            print(f"[ERROR] processing sensor batch: {e}")


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        print("Initializing Transaction Stream...")
        print(f"Stream ID: {self.stream_id}, Type: Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed_batches += 1
        try:
            print(f"Processing transaction batch: {data_batch}")
            self.processed_data = [*self.processed_data,
                                   f"{ft_len(data_batch)} "
                                   "operations processed"]
            print(f"Transaction analysis: {self.processed_data[-1]}")
        except Exception as e:
            print(f"[ERROR] processing transaction batch: {e}")


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        print("Initializing Event Stream...")
        print(f"Stream ID: {self.stream_id}, Type: System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed_batches += 1
        try:
            print(f"Processing event batch: {data_batch}")
            error_count = 0
            for data in data_batch:
                if "error" in data:
                    error_count += 1
            self.processed_data = [*self.processed_data,
                                   f"{ft_len(data_batch)} events processed"]
            print(f"Event analysis: {self.processed_data[-1]}, "
                  f"{error_count} error detected")
        except Exception as e:
            print(f"[ERROR] processing event batch: {e}")


class StreamProcessor:
    def __init__(self) -> None:
        self.streams = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams = [*self.streams, stream]

    def process_batches(self, batches: Dict[Any, List]) -> None:
        print()
        for stream, (criteria, data) in zip(self.streams, batches.items()):
            stream.process_batch(stream.filter_data(data, criteria))
            print()

    def get_stream_stats(self, batch: int) -> None:
        try:
            print(f"Batch {batch} Results: ")
            for stream in self.streams:
                stats = stream.get_stats()
                data = stats["processed_data"]
                if isinstance(stream, SensorStream):
                    print(f"- Sensor data: {data[batch - 1]}")
                elif isinstance(stream, TransactionStream):
                    print(f"- Transaction data: {data[batch - 1]}")
                elif isinstance(stream, EventStream):
                    print(f"- Event data: {data[batch - 1]}")
        except Exception as e:
            print(f"[ERROR] getting stream stats: {e}")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    sensor = SensorStream("SENSOR_001")
    transaction = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")

    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(transaction)
    processor.add_stream(event)

    batches = {
        None: ["temp:22.5", "humidity:65", "pressure:1013"],
        "buy": ["buy:100", "sell:150", "buy:75"],
        "error": ["login", "error", "logout"]
    }
    processor.process_batches(batches)
    processor.get_stream_stats(1)
    print("\nAll streams processed successfully. Nexus throughput optimal.")
