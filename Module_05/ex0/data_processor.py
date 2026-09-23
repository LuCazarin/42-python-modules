#!/usr/bin/env python3
"""Module for polymorphic data processors using Abstract Base Classes."""

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


def main() -> None:

    """Demonstrate DataProcessor architecture and test validation."""
    print("=== Code Nexus - Data Processor ===")
    print("\nTesting Numeric Processor...")
    num_proc = NumericProcessor()
    print(f"Trying to validate input '42': {num_proc.validate(42)}")
    print(f"Trying to validate input 'Hello': {num_proc.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_proc.ingest("foo")  # type: ignore[arg-type]
    except ValueError as e:
        print(f"Got exception: {e}")
    numeric_data: list[int | float] = [1, 2, 3, 4, 5]
    print(f"Processing data: {numeric_data}")
    num_proc.ingest(numeric_data)
    print("Extracting 3 values...")
    for _ in range(3):
        rank, val = num_proc.output()
        print(f"Numeric value {rank}: {val}")
    print("\nTesting Text Processor...")
    text_proc = TextProcessor()
    print(f"Trying to validate input '42': {text_proc.validate(42)}")
    text_data = ["Hello", "Nexus", "World"]
    print(f"Processing data: {text_data}")
    text_proc.ingest(text_data)
    print("Extracting 1 value...")
    rank, val = text_proc.output()
    print(f"Text value {rank}: {val}")
    print("\nTesting Log Processor...")
    log_proc = LogProcessor()
    print(f"Trying to validate input 'Hello': {log_proc.validate('Hello')}")
    log_data = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f"Processing data: {log_data}")
    log_proc.ingest(log_data)
    print("Extracting 2 values...")
    for _ in range(2):
        rank, val = log_proc.output()
        print(f"Log entry {rank}: {val}")


if __name__ == "__main__":
    main()
