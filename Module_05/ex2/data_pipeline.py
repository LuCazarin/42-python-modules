#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Protocol


class DataProcessor(ABC):
    """Abstract base class for data processing architecture."""

    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._rank_counter: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Check if the input data is appropriate for the current processor."""
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """Process and ingest the input data."""
        pass

    def output(self) -> tuple[int, str]:
        """Output the currently ingested data."""
        if not self._storage:
            raise IndexError("No data available in processor storage.")
        return self._storage.pop(0)


class NumericProcessor(DataProcessor):
    """Processor specialized in handling numeric data."""

    def validate(self, data: Any) -> bool:
        if isinstance(data, bool):
            return False
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            if not data:
                return False
            return all(
                isinstance(x, (int, float)) and not isinstance(x, bool)
                for x in data
            )
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._storage.append((self._rank_counter, str(item)))
                self._rank_counter += 1
        else:
            self._storage.append((self._rank_counter, str(data)))
            self._rank_counter += 1


class TextProcessor(DataProcessor):
    """Processor specialized in handling text data."""

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            if not data:
                return False
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self._storage.append((self._rank_counter, item))
                self._rank_counter += 1
        else:
            self._storage.append((self._rank_counter, data))
            self._rank_counter += 1


class LogProcessor(DataProcessor):
    """Processor specialized in handling log data."""

    def _is_valid_log_dict(self, item: Any) -> bool:
        if not isinstance(item, dict):
            return False
        return all(
            isinstance(k, str) and isinstance(v, str)
            for k, v in item.items()
        )

    def validate(self, data: Any) -> bool:
        if self._is_valid_log_dict(data):
            return True
        if isinstance(data, list):
            if not data:
                return False
            return all(self._is_valid_log_dict(x) for x in data)
        return False

    def _format_log(self, log_dict: dict[str, str]) -> str:
        if "log_level" in log_dict and "log_message" in log_dict:
            return f"{log_dict['log_level']}: {log_dict['log_message']}"
        return ": ".join(log_dict.values())

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for item in data:
                formatted = self._format_log(item)
                self._storage.append((self._rank_counter, formatted))
                self._rank_counter += 1
        else:
            formatted = self._format_log(data)
            self._storage.append((self._rank_counter, formatted))
            self._rank_counter += 1


class ExportPlugin(Protocol):
    """Protocol defining the export plugin interface."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CsvExportPlugin:
    """Export plugin for CSV format."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [val for _, val in data]
        print("CSV Output:")
        print(",".join(values))


class JsonExportPlugin:
    """Export plugin for JSON format."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        items = []
        for rank, val in data:
            items.append(f'"item_{rank}": "{val}"')
        print("JSON Output:")
        print("{" + ", ".join(items) + "}")


class DataStream:
    """Manages adaptive stream processing and routes data to processors."""

    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            processed = False
            for proc in self.processors:
                if proc.validate(element):
                    proc.ingest(element)
                    processed = True
                    break
            if not processed:
                print(
                    "DataStream error - "
                    f"Can't process element in stream: {element}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        for proc in self.processors:
            name = proc.__class__.__name__.replace("Processor", " Processor")
            print(
                f"{name}: total {proc._rank_counter} items processed, "
                f"remaining {len(proc._storage)} on processor"
            )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            batch: list[tuple[int, str]] = []
            for _ in range(nb):
                if proc._storage:
                    batch.append(proc.output())
            if batch:
                plugin.process_output(batch)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Processors")
    num_processor = NumericProcessor()
    text_processor = TextProcessor()
    log_processor = LogProcessor()
    stream.register_processor(num_processor)
    stream.register_processor(text_processor)
    stream.register_processor(log_processor)

    batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'
            },
            {
                'log_level': 'INFO',
                'log_message': 'User wil is connected'
            }
        ],
        42,
        ['Hi', 'five']
    ]
    print(f"\nSend first batch of data on stream: {batch}")
    stream.process_stream(batch)

    stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CsvExportPlugin()
    stream.output_pipeline(3, csv_plugin)

    stream.print_processors_stats()

    batch_2 = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {
                'log_level': 'ERROR',
                'log_message': '500 server crash'
            },
            {
                'log_level': 'NOTICE',
                'log_message': 'Certificate expires in 10 days'
            }
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]
    print(f"\nSend another batch of data: {batch_2}")
    stream.process_stream(batch_2)

    stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    json_plugin = JsonExportPlugin()
    stream.output_pipeline(5, json_plugin)

    stream.print_processors_stats()


if __name__ == "__main__":
    main()
