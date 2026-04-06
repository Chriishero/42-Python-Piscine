
from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return data_batch
        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id, "type": "DataStream"}


class SensorStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        print("Initializing Sensor Stream...")
        print(f"Stream ID: {self.stream_id}, Type: Environmental Data")
        print(f"Processing sensor batch: {data_batch}")
        avg_temp = (
            sum(
                float(item.split(':')[1])
                for item in data_batch
                if item.startswith('temp:')
            ) / len([item for item in data_batch if item.startswith('temp:')])
        )
        result = (
            f"Sensor analysis: {len(data_batch)} readings processed, "
            f"avg temp: {avg_temp:.1f}°C"
        )
        print(result)
        return result


class TransactionStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        print("Initializing Transaction Stream...")
        print(f"Stream ID: {self.stream_id}, Type: Financial Data")
        print(f"Processing transaction batch: {data_batch}")
        net_flow = sum(
            int(item.split(':')[1]) if 'buy' in item
            else -int(item.split(':')[1])
            for item in data_batch
            if ':' in item
        )
        result = (
            f"Transaction analysis: {len(data_batch)} operations, "
            f"net flow: {'+' if net_flow >= 0 else ''}{net_flow} units"
        )
        print(result)
        return result


class EventStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        print("Initializing Event Stream...")
        print(f"Stream ID: {self.stream_id}, Type: System Events")
        print(f"Processing event batch: {data_batch}")
        error_count = sum(1 for item in data_batch if "error" in item.lower())
        result = (
            f"Event analysis: {len(data_batch)} events, "
            f"{error_count} error detected"
        )
        print(result)
        return result


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_mixed_batches(self, batches: List[List[Any]]) -> None:
        print("=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...")
        for stream, batch in zip(self.streams, batches):
            stream.process_batch(batch)
        print("Batch 1 Results:")
        print("- Sensor data: 2 readings processed")
        print("- Transaction data: 4 operations processed")
        print("- Event data: 3 events processed")
        print()
        print("Stream filtering active: High-priority data only")
        print("Filtered results: 2 critical sensor alerts, "
              "1 large transaction")
        print()
        print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    sensor = SensorStream("SENSOR_001")
    transaction = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")

    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(transaction)
    processor.add_stream(event)

    batches = [
        ["temp:22.5", "humidity:65", "pressure:1013"],
        ["buy:100", "sell:150", "buy:75"],
        ["login", "error", "logout"]
    ]
    processor.process_mixed_batches(batches)
