#!/usr/bin/env python3

from abc import ABC, abstractmethod
import typing


class DataProcessor(ABC):
    """Abstract Base Class for all data processors."""

    def __init__(self) -> None:
        """Initialize common processor storage and rank counter."""
        self._storage: list[tuple[int, str]] = []
        self._rank_counter: int = 0

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        """Check whether input data is valid for this processor."""
        pass

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        """Process and store input data."""
        pass

    def output(self) -> tuple[int, str]:
        """Extract and remove oldest stored piece of data with rank."""
        if not self._storage:
            raise IndexError("No data available in processor storage.")
        return self._storage.pop(0)


class NumericProcessor(DataProcessor):
    """Processor for numeric data (ints, floats, and lists of numbers)."""

    def validate(self, data: typing.Any) -> bool:
        """Validate if data is int, float, or list of ints/floats."""
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
        """Ingest numeric data into internal string storage."""
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
    """Processor for text data (strings and lists of strings)."""

    def validate(self, data: typing.Any) -> bool:
        """Validate if data is str or list of strings."""
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            if not data:
                return False
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        """Ingest text data into internal storage."""
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
    """Processor for log dicts and lists of log dicts."""

    def _is_valid_log_dict(self, item: typing.Any) -> bool:
        """Check if an item is a valid string key-value dictionary."""
        if not isinstance(item, dict):
            return False
        return all(
            isinstance(k, str) and isinstance(v, str)
            for k, v in item.items()
        )

    def validate(self, data: typing.Any) -> bool:
        """Validate if data is a log dict or a list of log dicts."""
        if self._is_valid_log_dict(data):
            return True
        if isinstance(data, list):
            if not data:
                return False
            return all(self._is_valid_log_dict(x) for x in data)
        return False

    def _format_log(self, log_dict: dict[str, str]) -> str:
        """Format a log dict into a standard string representation."""
        if "log_level" in log_dict and "log_message" in log_dict:
            return f"{log_dict['log_level']}: {log_dict['log_message']}"
        return ": ".join(log_dict.values())

    def ingest(
        self, data: dict[str, str] | list[dict[str, str]]
    ) -> None:
        """Ingest log dictionary data into internal storage."""
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


class DataStream:
    """Manages adaptive stream processing and routes data to processors."""

    def __init__(self) -> None:
        """Initialize the data stream with an empty list of processors."""
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        """Register a new data processor to handle incoming stream data."""
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        """Route each element of the stream to the appropriate processor."""
        for element in stream:
            processed: bool = False
            for proc in self.processors:
                if proc.validate(element):
                    proc.ingest(element)
                    processed = True
                    break
            if not processed:
                print(f"DataStream error - Can't process "
                      f"element in stream: {element}")

    def print_processors_stats(self) -> None:
        """Print statistics for all registered data processors."""
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        for proc in self.processors:
            name: str = proc.__class__.__name__.replace("Processor",
                                                        " Processor")
            print(
                f"{name}: total {proc._rank_counter} items processed, "
                f"remaining {len(proc._storage)} on processor"
            )


def main() -> None:
    """Demonstrate DataStream architecture and polymorphic processing."""
    print("=== Code Nexus - Data Stream ===")
    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Numeric Processor")
    num_processor = NumericProcessor()
    stream.register_processor(num_processor)

    batch: list[typing.Any] = [
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

    print("\nRegistering other data processors")
    text_processor = TextProcessor()
    log_processor = LogProcessor()
    stream.register_processor(text_processor)
    stream.register_processor(log_processor)

    print("Send the same batch again")
    stream.process_stream(batch)

    stream.print_processors_stats()

    print(
        "\nConsume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )
    for _ in range(3):
        num_processor.output()
    for _ in range(2):
        text_processor.output()
    for _ in range(1):
        log_processor.output()

    stream.print_processors_stats()


if __name__ == "__main__":
    main()
