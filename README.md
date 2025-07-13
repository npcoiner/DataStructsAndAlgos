# DataStructsAndAlgos

This is my long-term personal reference repository for fundamental **data structures**, **algorithms**, and **machine learning techniques** implemented from scratch in multiple languages.

Each folder is organized by **concept first** (e.g. `heap/`, `linked_list/`, `k_means/`), and may contain multiple **language-specific implementations** along with **localized test files**. This structure allows quick access, comparison, and reuse across different programming contexts.

## Project Structure

```
DataStructsAndAlgos/
├── README.md
├── linked_list/
│   ├── linked_list.py
│   ├── linked_list.zig
│   └── tests/
│       └── test_linked_list.py
├── heap/
│   ├── binary_heap.py
│   ├── binary_heap.rs
│   └── tests/
│       └── test_binary_heap.py
├── k_means/
│   ├── k_means.py
│   └── tests/
│       └── test_k_means.py
└── ...
```

Each concept folder contains:
- One or more implementations: `*.py`, `*.zig`, `*.cpp`, `*.rs`, etc.
- Local `tests/` directory with matching test scripts
- Optional `README.md` per concept: outlines complexity, sources, and notes

---

## Conventions

- Use clear, idiomatic code in each language — not just translations.
- Keep tests **local per concept** to avoid test runner collisions.
- Prefer **standalone files**: no shared framework or imports across folders.
- Add complexity tables, edge case notes, and reference links where useful.
- Use docstrings and inline comments to explain design decisions.

---

## Testing

| Language | Run Tests With                |
|----------|-------------------------------|
| Python   | `pytest [folder]/tests`       |
| Zig      | `zig test [impl].zig`         |
| C++      | `g++ && ./a.out` (or Catch2)  |
| Rust     | `cargo test` (if used)        |

> Each implementation should be verifiable in isolation.

---

## Topics Covered

| Concept            | Status         | Notes                    |
|--------------------|----------------|---------------------------|
| Linked List        |       | Basic and doubly linked  |
| Binary Heap        |        | Min/Max + heapify        |
| K-Means Clustering |            | From scratch             |
| ...                |   |                          |

---

## Sources & References

- *CLRS – Introduction to Algorithms*
- LeetCode, NeetCode, Competitive Programming books
- Research papers 

---

## License

MIT — use, copy, and adapt freely. If you find this useful, feel free to fork, star, or reference.

---

Built and maintained by [npcoiner].

